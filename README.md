<div align="center">

```
:::::  ::    ::   ::::        ::::   :::::  :::::   ::      ::  :::::    :::::
::  :  :: .  ::   ::  .       ::  .  ::___  ::   :  ::     ::   ::___    ::   :
::  :  ::  . ::  .  ::        . ::   ::     :::::     :: ::     ::       :::::
:::::  ::   .::   ::::        ::::   :::::  ::   .      :       :::::    ::   .
```

# 🌐 DNS Server — Hostname to IPv4 Resolver

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square&logo=windows)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen?style=flat-square)]()
[![Author](https://img.shields.io/badge/Author-Mudasir%20Zia-purple?style=flat-square)](https://github.com/CyberBros435)

> **A lightweight, terminal-based DNS lookup tool built in Python.**  
> Instantly resolve any hostname to its IPv4 address using `nslookup` — right from your terminal.

</div>

---

## 📌 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Requirements](#-requirements)
- [Quick Install (One Command)](#-quick-install-one-command)
- [Step-by-Step Installation](#-step-by-step-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Related Projects](#-related-projects)
- [Author](#-author)
- [Disclaimer](#-disclaimer)

---

## 🧠 About

**DNS Server** is a simple but effective Python CLI tool that lets you resolve any domain or hostname to its IPv4 address using Windows' built-in `nslookup` command.

It features a clean loop-based interface — enter as many hostnames as you want, one after another, without restarting the tool. Perfect for **network learners, CTF players, and sysadmins** who need quick DNS lookups from the terminal.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔎 **DNS Lookup** | Resolve any hostname to IPv4 via `nslookup` |
| 🔁 **Loop Mode** | Continuously query hostnames without restarting |
| 🛡️ **Input Validation** | Rejects numeric-only and empty inputs gracefully |
| 🎨 **Colorized CLI** | Clean, color-coded terminal output via `colorama` |
| ❌ **Safe Exit** | Type `q` to exit lookup, or `n` to stop the session |

---

## ⚙️ Requirements

- **OS:** Windows (uses `nslookup` from `C:\Windows\system32`)
- **Python:** 3.7 or higher
- **Internet / Wi-Fi:** Must be active for DNS resolution
- **Dependencies:**
  - [`colorama`](https://pypi.org/project/colorama/) — terminal color support

---

## ⚡ Quick Install (One Command)

```bash
git clone https://github.com/CyberBros435/DNS_Server.git && cd DNS_Server && pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

---

## 🛠️ Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/CyberBros435/DNS_Server.git
```

### 2. Navigate into the Project Directory

```bash
cd DNS_Server
```

### 3. (Optional) Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install colorama
```

### 5. Run the Tool

```bash
python main.py
```

---

## 🚀 Usage

When you run the tool, you'll be prompted to continue the session:

```
[ + ]  Do You want to Continue (y/n)
```

Type `y` to start a DNS lookup:

```
[ + ]  Enter the hostname (e.g: google.com)(q to exit)
```

### Example Session

```
[ + ]  Do You want to Continue (y/n)   y

[ + ]  Enter the hostname (e.g: google.com)(q to exit)   google.com

Changing directory

Server:  dns.google
Address:  8.8.8.8

Non-authoritative answer:
Name:    google.com
Address: 142.250.190.14

[ + ]  Do You want to Continue (y/n)   y

[ + ]  Enter the hostname (e.g: google.com)(q to exit)   q

Exiting

[ + ]  Do You want to Continue (y/n)   n

Exiting...
```

### Input Rules

| Input | Behavior |
|---|---|
| `google.com` | Resolves hostname via `nslookup` |
| `123` (digits only) | Rejected — invalid hostname type |
| `q` | Exits the current lookup, returns to continue prompt |
| `n` (at continue prompt) | Exits the program entirely |

---

## 🔬 How It Works

1. The tool prompts whether you want to continue the session (`y/n`).
2. On `y`, it asks for a hostname input.
3. It validates the input — rejects pure numeric strings.
4. Changes directory to `C:\Windows\system32` and runs:

```bash
nslookup <hostname>
```

5. The result (DNS records, resolved IP) is printed directly to the terminal.
6. The loop continues until the user exits.

---

## 📁 Project Structure

```
DNS_Server/
│
├── main.py               # Main entry point & DNS logic
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🔗 Related Projects

> Part of the **CyberBros435** network toolkit collection:

| Tool | Description | Link |
|---|---|---|
| 🔍 **IP Scanner** | IPv4 scanner, ping, tracert & ipconfig tool | [CyberBros435/IP_Scanner](https://github.com/CyberBros435/IP_Scanner) |
| 🌐 **DNS Server** | Hostname to IPv4 resolver *(this repo)* | [CyberBros435/DNS_Server](https://github.com/CyberBros435/DNS_Server) |

---

## 👤 Author

**Mudasir Zia**  
🔗 GitHub: [@CyberBros435](https://github.com/CyberBros435)  
📦 Repository: [CyberBros435/DNS_Server](https://github.com/CyberBros435/DNS_Server)

---

## ⚠️ Disclaimer

> This tool is intended **for educational and authorized network diagnostic purposes only.**  
> The author is **not responsible** for any misuse of this software.  
> Always ensure you have **explicit permission** before performing DNS lookups or network reconnaissance on systems you do not own.

---

<div align="center">

Made with ❤️ by [Mudasir Zia](https://github.com/CyberBros435) · ⭐ Star this repo if you found it useful!

</div>
