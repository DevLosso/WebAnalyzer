"""
<--------------------------INFO-------------------------->
Project: WebAnalyzer
Module: CheakSite.py
Author: Alireza Abaspour
Owner: DevLosso
Team: DevLossoTM
Date: 2026-07-02
Description: Analyze any website's SEO health in seconds — get a score, spot the issues, fix them fast.
<-------------------------------------------------------->
"""

import asyncio
import re
from collections import Counter

import aiohttp
from bs4 import BeautifulSoup
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/137 Safari/537.36"
}
TIMEOUT = aiohttp.ClientTimeout(total=30)


class SEOAnalyzer:
    def __init__(self, url: str):
        self.url = url

    async def fetch(self) -> str:
        async with aiohttp.ClientSession(headers=HEADERS, timeout=TIMEOUT) as session:
            async with session.get(self.url, allow_redirects=True) as resp:
                resp.raise_for_status()
                return await resp.text()

    @staticmethod
    def parse_html(html: str) -> dict:
        soup = BeautifulSoup(html, "lxml")

        title = soup.title.text.strip() if soup.title else "Missing"
        h1_count = len(soup.find_all("h1"))
        has_meta = soup.find("meta", attrs={"name": "description"}) is not None
        missing_alt = sum(not img.get("alt") for img in soup.find_all("img"))

        penalties = (
            15 * (h1_count != 1)
            + 20 * (title == "Missing")
            + 10 * (not has_meta)
            + min(missing_alt, 15)
        )

        return {
            "title": title,
            "h1": h1_count,
            "missing_alt": missing_alt,
            "score": max(100 - penalties, 0),
            "tags": Counter(tag.name for tag in soup.find_all(True)),
        }

    async def analyze(self) -> dict:
        with console.status("[bold green]Fetching Website..."):
            html = await self.fetch()
        return await asyncio.to_thread(self.parse_html, html)

    @staticmethod
    def show(result: dict) -> None:
        table = Table("Tag", "Count", title="HTML Tags")
        for tag, count in result["tags"].most_common(15):
            table.add_row(tag, str(count))
        console.print(table)

        console.print(Panel(
            f"[green]SEO Score:[/green] {result['score']}/100\n\n"
            f"[cyan]Title:[/cyan] {result['title']}\n\n"
            f"[yellow]H1 Count:[/yellow] {result['h1']}\n\n"
            f"[magenta]Images Without ALT:[/magenta] {result['missing_alt']}",
            title="AI SEO Report",
            border_style="green",
        ))


def normalize_url(url: str) -> str:
    url = re.sub(
        r"^(https?)[:/]*",
        lambda m: m.group(1).lower() + "://",
        url.strip(),
        flags=re.IGNORECASE,
    )
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"
    return url


async def main() -> None:
    url = normalize_url(input("URL: "))

    try:
        analyzer = SEOAnalyzer(url)
        analyzer.show(await analyzer.analyze())
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")


if __name__ == "__main__":
    asyncio.run(main())
    
    