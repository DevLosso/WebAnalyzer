# WebAnalyzer
A Python-based web analysis tool for extracting site data (HTML tags) for SEO.
# 🔎 WebAnalyzer

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![SEO](https://img.shields.io/badge/SEO-Analyzer-orange)
![CLI](https://img.shields.io/badge/interface-CLI-lightgrey)

A fast and lightweight **SEO website analyzer** built with Python.

WebAnalyzer fetches a webpage, analyzes its HTML structure, compares SEO elements against configurable standards, and generates a clean terminal report.

Perfect for developers, SEO specialists, and technical auditors.

---

# ✨ Features

✅ Asynchronous website fetching  
✅ SEO tag analysis  
✅ Clean CLI output with **Rich**  
✅ Configurable SEO standards  
✅ Automatic SEO scoring  
✅ Lightweight and fast  

The analyzer checks:

- `title` tag
- `meta description`
- `h1 / h2 / h3` structure
- images without `alt`
- number of links
- paragraph count
- general HTML structure

---

# 📂 Project Structure
WebAnalyzer

│

├── cheakSite.py

├── seo_standards.json

├── requirements.txt

└── README.md

text

---

# ⚙️ How It Works

1️⃣ User enters a website URL  
2️⃣ Script downloads the page asynchronously  
3️⃣ HTML is parsed using BeautifulSoup  
4️⃣ Important SEO elements are extracted  
5️⃣ Results are compared with `seo_standards.json`  
6️⃣ A final **SEO score and report** is generated  

---

# 📊 Example Output

Example terminal report:
SEO Report
Title Tag: ✅ Found

Meta Description: ✅ Found

H1 Tags: 1

H2 Tags: 6

Images: 12

Images Missing ALT: 2

SEO Score: 87 / 100

text

Output is displayed in a **clean styled terminal panel** using the `rich` library.

---

# 🚀 Installation

## 1️⃣ Clone the repository
bash
git clone https://github.com/your-username/WebAnalyzer.git
cd WebAnalyzer
2️⃣ Create virtual environment (recommended)
Linux / macOS
bash
python3 -m venv venv
source venv/bin/activate
Windows
bash
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
Automatic installation
bash
pip install -r requirements.txt
📦 Requirements
Create a file called requirements.txt

txt
aiohttp
beautifulsoup4
lxml
rich
📥 Manual Installation
If you prefer installing packages manually:

bash
pip install aiohttp
pip install beautifulsoup4
pip install lxml
pip install rich
▶️ Run the Analyzer
bash
python cheakSite.py
Enter the website URL when prompted:

text
https://example.com
The tool will analyze the page and display a full SEO report.

🧠 SEO Standards Configuration
SEO rules are defined inside:

text
seo_standards.json
Example:

json
{
  "h1": {"min": 1, "max": 1},
  "h2": {"min": 2, "max": 10},
  "h3": {"min": 2, "max": 20},
  "img": {"min": 1, "max": 100},
  "a": {"min": 5, "max": 200},
  "p": {"min": 5, "max": 1000}
}
You can modify this file to change the SEO analysis logic.

🛠 Future Improvements
Possible upgrades:

Export report to JSON
Export report to CSV
Batch website scanning
Detect OpenGraph tags
Detect Twitter cards
Sitemap detection
robots.txt analysis
Page speed insights
GUI version
📚 Technologies Used
Python
aiohttp
BeautifulSoup
Rich
Asyncio
JSON
🤝 Contributing
Contributions are welcome.

If you’d like to improve the project:

Fork the repository
Create a new branch
Make your changes
Submit a pull request
📜 License
This project is released under the MIT License.

👨‍💻 Author
Developed as a Python SEO analysis tool for learning, automation, and website inspection.
