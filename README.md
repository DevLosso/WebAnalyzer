<div align="center">

# 🚀 CheakSite — AI SEO Analyzer

### ⚡ Lightning-fast, async-powered SEO auditing right from your terminal

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Async](https://img.shields.io/badge/Async-aiohttp-2C5BB4?style=for-the-badge&logo=aiohttp&logoColor=white)](https://docs.aiohttp.org/)
[![UI](https://img.shields.io/badge/Terminal_UI-Rich-FAE042?style=for-the-badge)](https://github.com/Textualize/rich)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](#-license)

**Analyze any website's SEO health in seconds — get a score, spot the issues, fix them fast.**

*Built with ❤️ by [DevLosso](https://github.com/DevLosso)*

</div>

---

## ✨ Features

- ⚡ **Fully Asynchronous** — non-blocking fetching with `aiohttp` + `asyncio` for maximum speed
- 🎯 **SEO Score (0–100)** — instant, weighted scoring based on real SEO best practices
- 🏷️ **Full HTML Tag Analysis** — counts and ranks every tag on the page
- 📝 **Title Tag Detection** — flags missing or empty `<title>` tags
- 🔖 **Meta Description Check** — verifies the presence of the meta description
- 🖼️ **ALT Attribute Audit** — finds every image missing its `alt` text (accessibility + SEO win)
- 📊 **Beautiful Terminal Reports** — gorgeous tables and panels powered by [Rich](https://github.com/Textualize/rich)
- 🧵 **Smart Threading** — HTML parsing runs in an executor so the event loop never blocks
- 🔁 **Auto HTTPS & Redirects** — just type the domain, the tool handles the rest
- 📏 **Configurable Standards** — tune SEO thresholds via `seo_standards.json`

---

## 🖥️ Demo

```
URL: example.com

⠋ Fetching Website...

        HTML Tags
┏━━━━━━━━┳━━━━━━━┓
┃ Tag    ┃ Count ┃
┡━━━━━━━━╇━━━━━━━┩
│ div    │ 142   │
│ a      │ 67    │
│ p      │ 34    │
│ img    │ 21    │
│ ...    │ ...   │
└────────┴───────┘

╭────────────── AI SEO Report ──────────────╮
│ SEO Score: 85/100                         │
│                                           │
│ Title: Example Domain                     │
│                                           │
│ H1 Count: 1                               │
│                                           │
│ Images Without ALT: 3                     │
╰───────────────────────────────────────────╯
```

---

## 📦 Installation

**1. Clone the repository**

```bash
git clone https://github.com/DevLosso/cheakSite.git
cd cheakSite
```

**2. Install dependencies**

```bash
pip install aiohttp beautifulsoup4 lxml rich
```

> 💡 **Tip:** Use a virtual environment to keep things clean:
> ```bash
> python -m venv venv
> source venv/bin/activate   # Windows: venv\Scripts\activate
> ```

---

## 🚀 Usage

```bash
python cheakSite.py
```

Then simply enter any URL — with or without `https://`:

```
URL: github.com
```

That's it. Sit back and watch the magic happen. ✨

---

## 🧮 How the Scoring Works

Every audit starts at a perfect **100** and deducts points for issues found:

| Check | Condition | Penalty |
|:------|:----------|:-------:|
| 🏷️ **H1 Heading** | Not exactly one `<h1>` | **−15** |
| 📝 **Title Tag** | Missing `<title>` | **−20** |
| 🔖 **Meta Description** | Missing meta description | **−10** |
| 🖼️ **Image ALT Text** | Each image without `alt` | **−1** (capped at −15) |

> The score never drops below **0** — but if it gets close, your site needs serious love. 😅

---

## ⚙️ SEO Standards Config

The `seo_standards.json` file defines the recommended min/max range for key SEO elements — a reference ruleset for extending the analyzer:

```json
{
  "h1":    { "min": 1, "max": 1 },
  "h2":    { "min": 2, "max": 10 },
  "h3":    { "min": 2, "max": 20 },
  "title": { "min": 1, "max": 1 },
  "meta":  { "min": 1, "max": 20 },
  "img":   { "min": 1, "max": 100 },
  "a":     { "min": 5, "max": 200 },
  "p":     { "min": 5, "max": 1000 }
}
```

| Element | Why it matters |
|:--------|:---------------|
| `h1` | Exactly **one** H1 per page — it's your page's headline |
| `h2` / `h3` | Well-structured content hierarchy boosts readability & rankings |
| `title` | The single most important on-page SEO element |
| `meta` | Meta tags feed search engines & social previews |
| `img` | Visual content improves engagement (with proper ALT text!) |
| `a` | Internal & external links build authority |
| `p` | Enough textual content signals real value to crawlers |

---

## 🏗️ Architecture

```
cheakSite.py
│
├── SEOAnalyzer
│   ├── fetch()        →  async HTTP GET with browser-like headers & 30s timeout
│   ├── parse_html()   →  BeautifulSoup + lxml parsing, tag counting, scoring
│   ├── analyze()      →  orchestrates fetch + parses in a thread executor
│   └── show()         →  renders Rich tables & the final report panel
│
└── seo_standards.json →  configurable SEO threshold rules
```

**Why async?** Network I/O is the slowest part of any crawler. By using `aiohttp`, the fetch never blocks — and heavy HTML parsing is offloaded to a thread executor via `run_in_executor`, keeping the event loop buttery smooth. 🧈

---

## 🛠️ Tech Stack

| Technology | Role |
|:-----------|:-----|
| **Python 3.9+** | Core language |
| **aiohttp** | Async HTTP client |
| **BeautifulSoup4 + lxml** | Blazing-fast HTML parsing |
| **Rich** | Stunning terminal UI |
| **asyncio** | Concurrency engine |

---

## 🗺️ Roadmap

- [ ] Enforce full `seo_standards.json` rules (h2/h3/link/paragraph ranges)
- [ ] Batch mode — analyze multiple URLs concurrently
- [ ] Export reports to JSON / HTML / PDF
- [ ] Page speed & Core Web Vitals checks
- [ ] Open Graph & Twitter Card validation
- [ ] Broken link detection
- [ ] CLI arguments (`cheaksite <url> --json`)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. 🍴 Fork the repo
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 🚀 Push and open a Pull Request

---

## 📄 License

Released under the **MIT License** — free to use, modify, and share.

---

<div align="center">

### ⭐ If this tool helped you, give it a star!

**Made with 💚 and lots of ☕ by [DevLosso](https://github.com/DevLosso)**

</div>
