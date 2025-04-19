# Network Tool (Tkinter GUI)

A simple Python GUI application for basic network diagnostic tools using `tkinter` and `subprocess`.

## 🛠 Features

- **Ping an address**
- **WHOIS lookup**
- **DNS Lookup (nslookup)**
- **Traceroute**
- **Get Public IP Address**

## 🖥️ GUI Overview

The app features a graphical interface where users can:
- Select a command from a list
- Enter a target IP address or domain (if required)
- View the command output directly in the GUI

## 📦 Requirements

- Python 3.x
- Modules: `tkinter` (standard), `subprocess`

> On Windows, you may need to adjust some commands like:
> - `ping -c` → `ping -n`
> - `traceroute` → `tracert`
