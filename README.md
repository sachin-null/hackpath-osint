# 🌐 HackPath OSINT Tool v2

> **10-in-1 OSINT reconnaissance toolkit**
> Created by **Sachin Ser** | HackPath

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://python.org)
[![Version](https://img.shields.io/badge/Version-2.0-cyan?style=flat-square)](https://github.com/sachin-null/hackpath-osint)
[![Platform](https://img.shields.io/badge/Platform-Termux%20|%20Linux%20|%20Kali-orange?style=flat-square)](https://github.com/sachin-null)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

---

## ⚡ All 10 Tools

| # | Tool | Features |
|---|------|---------|
| 1 | 🔍 **My IP Info** | IP, location, ISP, proxy detect, Google Maps |
| 2 | 🌍 **IP Lookup** | Any IP — country, city, ASN, reverse DNS |
| 3 | 🌐 **Domain Info** | DNS, headers, robots.txt, admin check |
| 4 | 📡 **DNS Lookup** | A/MX/NS/TXT/CNAME/SOA/PTR records |
| 5 | 🔓 **Port Scanner** | Top 20/100/custom ports |
| 6 | 📧 **Email Header** | Spam check, sender IP lookup |
| 7 | 🔗 **URL Analyzer** | Phishing detection, risk level |
| 8 | 🔎 **Subdomain Finder** | 50+ common subdomains check ★NEW |
| 9 | 📋 **WHOIS Lookup** | Registration, expiry via RDAP ★NEW |
| 10 | 🔮 **Google Dorks** | 18 dork templates generator ★NEW |

---

## 📌 What's New in v2?

- Subdomain Finder (50+ subdomains)
- WHOIS Lookup via RDAP (no library needed)
- Google Dorks Generator (18 templates)
- HTTP security header detection
- Hidden page discovery (admin/git/phpmyadmin)
- Better IP geolocation with continent
- URL encoded character detection
- Save results to file

---

## 📲 Install & Run

### Termux
```bash
pkg install python git -y
git clone https://github.com/sachin-null/hackpath-osint
cd hackpath-osint
python3 osint.py
```

### Kali / Linux
```bash
git clone https://github.com/sachin-null/hackpath-osint
cd hackpath-osint
python3 osint.py
```

---

## 🖥️ Menu

```
  [1]  My IP Info
  [2]  IP Address Lookup
  [3]  Domain Information
  [4]  DNS Lookup
  [5]  Port Scanner
  [6]  Email Header Analyzer
  [7]  URL Analyzer
  [8]  Subdomain Finder   ★ NEW
  [9]  WHOIS Lookup       ★ NEW
  [10] Google Dorks       ★ NEW
  [0]  Exit
```

---

## 🔮 Google Dorks Examples

```
site:target.com inurl:admin
site:target.com filetype:pdf
site:target.com "index of"
site:target.com inurl:config
"target.com" site:pastebin.com
```

---

## 📦 Requirements

```
Python 3.x only · Zero extra packages · Works offline (partial)
Internet needed for IP/DNS/WHOIS lookups
```

---

## 🔄 Changelog

### v2.0
- 10 tools (was 7)
- Subdomain Finder
- WHOIS Lookup
- Google Dorks Generator
- Better domain checks

### v1.0
- Initial 7 tools

---

## ⚠️ Disclaimer

> Authorized / Educational use only.

---

## 👤 Created by

**Sachin Ser** | [HackPath](https://github.com/sachin-null)

---

## 🔗 More Tools

| Tool | Repo |
|------|------|
| 🔓 CTF Helper v2 | [hackpath-ctf-helper](https://github.com/sachin-null/hackpath-ctf-helper) |
| 🔐 PassGen v2 | [hackpath-passgen](https://github.com/sachin-null/hackpath-passgen) |
| 📋 Wordlist Maker v2 | [hackpath-wordlist-maker](https://github.com/sachin-null/hackpath-wordlist-maker) |
| 📱 Phone Analyzer v2 | [hackpath-phone-analyzer](https://github.com/sachin-null/hackpath-phone-analyzer) |
| 🕵️ Username OSINT | [hackpath-osint](https://github.com/sachin-null/hackpath-osint) |

<div align="center">

**⭐ Star this repo!**

`Made with ❤️ by Sachin Ser | HackPath`

</div>
