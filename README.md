ঠিক আছে, একটি ফাইলেই সব দিয়ে দিচ্ছি। এই ফাইলটি সরাসরি GitHub-এ upload করলেই সুন্দর দেখাবে।

README.md (একটি ফাইলেই সব)

```markdown
<!-- 
==================================================================
  ████████╗██╗  ██╗██╗  ████████╗ ██████╗ ██╗  ██╗
  ╚══██╔══╝██║  ██║██║  ╚══██╔══╝██╔═══██╗██║ ██╔╝
     ██║   ███████║██║     ██║   ██║   ██║█████╔╝ 
     ██║   ██╔══██║██║     ██║   ██║   ██║██╔═██╗ 
     ██║   ██║  ██║██║     ██║   ╚██████╔╝██║  ██╗
     ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝ ╚═╝  ╚═╝
==================================================================
-->

<div align="center">

<!-- LOGO -->
<img src="https://i.postimg.cc/W3BFvJ3B/file-0000000036dc723086051b0062570aaf.png" 
     alt="TikTok Toolkit Logo" 
     width="180" 
     height="180"/>

# ⚡ TIKTOK DATA TOOLKIT

### 🚀 Termux Optimized | 100% Working | Hacker Style

[![Version](https://img.shields.io/badge/version-3.0-blue?style=for-the-badge)](https://github.com/asif-6767)
[![Python](https://img.shields.io/badge/python-3.7+-green?style=for-the-badge)](https://www.python.org/)
[![Termux](https://img.shields.io/badge/platform-Termux-orange?style=for-the-badge)](https://termux.com/)
[![Status](https://img.shields.io/badge/status-stable-brightgreen?style=for-the-badge)](https://github.com/asif-6767)

**Developed by [ᴀꜱɪꜰ ɪꜱʟᴀᴍ](https://github.com/asif-6767)**

</div>

---

## 📌 FEATURES

```text
┌─────────────────────────────────────────────────────────────┐
│  ✅ 100% Working TikTok Data Scraper                       │
│  🔍 Fetch Complete User Information                        │
│  📊 Beautiful Formatted Output                             │
│  🖼️ Download Profile Pictures                              │
│  📝 Bulk Username Scraper                                  │
│  🎨 Hacker-Style Matrix Animations                         │
│  💾 Save Results as JSON                                   │
│  🚀 Fully Optimized for Termux                             │
└─────────────────────────────────────────────────────────────┘
```

---

📦 INSTALLATION

Step 1: Update Termux

```bash
pkg update && pkg upgrade -y
```

Step 2: Install Required Packages

```bash
pkg install python git -y
```

Step 3: Clone Repository

```bash
git clone https://github.com/asif-6767/tiktok-data.git
```

Step 4: Navigate to Directory

```bash
cd tiktok-data
```

Step 5: Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

🚀 HOW TO RUN

Just Type:

```bash
python tikdata.py
```

---

📊 OUTPUT EXAMPLE

```text
╔══════════════════════════════════════════════════════════════╗
║  ████████╗██╗  ██╗██╗  ████████╗ ██████╗ ██╗  ██╗          ║
║  ╚══██╔══╝██║  ██║██║  ╚══██╔══╝██╔═══██╗██║ ██╔╝          ║
║     ██║   ███████║██║     ██║   ██║   ██║█████╔╝           ║
║     ██║   ██╔══██║██║     ██║   ██║   ██║██╔═██╗           ║
║     ██║   ██║  ██║██║     ██║   ╚██████╔╝██║  ██╗          ║
║     ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝ ╚═╝  ╚═╝          ║
╠══════════════════════════════════════════════════════════════╣
║        Public Data Toolkit v3.0                             ║
║     ⚡ by ᴀꜱɪꜰ ɪꜱʟᴀᴍ ⚡                                   ║
╚══════════════════════════════════════════════════════════════╝

┌────────────────────────────────────────────────────────┐
│  📊 PROFILE DATA                                      │
├────────────────────────────────────────────────────────┤
│  ID     : 123456789                                   │
│  User   : @tiktok_user                               │
│  Name   : TikTok User                                │
│  Verify : ✅                                          │
│  Private: 🔓                                          │
│  Region : US                                          │
├────────────────────────────────────────────────────────┤
│  STATS                                                │
├────────────────────────────────────────────────────────┤
│  👥 Followers : 1000000                               │
│  👤 Following : 1000                                  │
│  ❤️ Likes     : 5000000                               │
│  🎬 Videos    : 100                                   │
│  🤝 Friends   : 500                                   │
├────────────────────────────────────────────────────────┤
│  BIO                                                  │
├────────────────────────────────────────────────────────┤
│  Just a regular TikTok user 🚀                       │
├────────────────────────────────────────────────────────┤
│  SOCIAL                                               │
├────────────────────────────────────────────────────────┤
│  • 📸 IG: @instagram_user                            │
│  • ▶️ YT: @youtube_user                              │
│  • 🐦 X: @twitter_user                               │
└────────────────────────────────────────────────────────┘
```

---

📁 PROJECT STRUCTURE

```text
tiktok-data/
├── README.md          # This file
├── requirements.txt   # Python dependencies
├── tikdata.py         # Main script
└── pp_images/         # Downloaded profile pictures
```

---

🛠️ DEPENDENCIES

Package Version Purpose
requests =2.28.0 HTTP requests
beautifulsoup4 =4.11.0 HTML parsing
lxml =4.9.0 XML/HTML parser

---

⚡ QUICK COMMANDS

```bash
# Install
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/asif-6767/tiktok-data.git
cd tiktok-data
pip install -r requirements.txt

# Run
python tikdata.py

# Update
git pull

# Uninstall
cd ..
rm -rf tiktok-data
```

---

📝 MENU OPTIONS

```text
┌────────────────────────────────────────────────────────┐
│  ╭──────────────────────────────────────────╮        │
│  │  1  ›  User Lookup              👤      │        │
│  │  2  ›  Bulk Scraper             📊      │        │
│  │  3  ›  Exit                     🚪      │        │
│  ╰──────────────────────────────────────────╯        │
└────────────────────────────────────────────────────────┘
```

---

🔧 TROUBLESHOOTING

❌ Error: "No module named 'requests'"

```bash
pip install requests
```

❌ Error: "No module named 'bs4'"

```bash
pip install beautifulsoup4
```

❌ Error: "No module named 'lxml'"

```bash
pip install lxml
```

❌ Error: "Permission denied"

```bash
chmod +x tikdata.py
python tikdata.py
```

---

⚠️ DISCLAIMER

```text
⚠️ This tool is for educational purposes only.
⚠️ Use responsibly and respect TikTok's terms of service.
⚠️ The developer is not responsible for any misuse.
```

---

📞 CONTACT

<div align="center">

Developed with ❤️ by ᴀꜱɪꜰ ɪꜱʟᴀᴍ

https://img.shields.io/badge/GitHub-asif--6767-black?style=for-the-badge&logo=github
https://img.shields.io/badge/Instagram-@asif__islam__-red?style=for-the-badge&logo=instagram
https://img.shields.io/badge/Telegram-@asif__islam-blue?style=for-the-badge&logo=telegram

</div>

---

<!--
==================================================================
  ⚡ END OF README
  © 2024 ᴀꜱɪꜰ ɪꜱʟᴀᴍ
==================================================================
-->

```

এই **README.md** ফাইলটি সরাসরি আপনার GitHub রিপোজিটরিতে আপলোড করুন। এটি HTML + Markdown মিক্সড, তাই GitHub-এ খুব সুন্দর দেখাবে। সব ইমোজি, কালার, বক্স, এবং ফরম্যাটিং ঠিক মতো কাজ করবে। 🚀
