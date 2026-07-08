# OCMOSS

**Observe • Control • Monitor Operating System**

OCMOSS is an open-source Windows Operating System Monitoring SDK written in Python. It provides a simple and modular interface for retrieving operating system lifecycle events, process information, and network information that are often difficult to access through standard Windows utilities.

---

# Features

## Version 1.0 – Operating System Lifecycle

- System Started
- Last Shutdown
- Current Uptime
- Last Restart
- Sleep Started
- Wake Up
- Power Source Changed

---

## Version 2.0 – Process Monitoring

- Running Applications
- Process Count
- Process Memory Usage

---

## Version 3.0 – Network Monitoring

- Network Information
- Internet Status
- IP Address
- Wi-Fi Information
- Wi-Fi Passwords

---

# Supported Platform

Operating System

- Windows 10
- Windows 11

Python

- Python 3.11 or later

---

# Installation

```bash
pip install ocmoss
```

---

# Quick Start

```python
import ocmoss

print(ocmoss.__version__)
```

---

# Project Structure

```text
OCMOSS
│
├── ocmoss
│   ├── core
│   ├── events
│   ├── windows
│   └── __init__.py
│
├── examples
├── tests
├── main.py
├── pyproject.toml
├── README.md
├── LICENSE
└── NOTICE
```

---

# Modules

## Operating System Lifecycle

- SystemStarted
- LastShutdown
- CurrentUptime
- LastRestart
- SleepStarted
- WakeUp
- PowerSourceChanged

## Process Monitoring

- RunningApplications
- ProcessCount
- ProcessMemoryUsage

## Network Monitoring

- NetworkInformation
- InternetStatus
- IPAddress
- WiFiInformation
- WiFiPasswords

---

# Roadmap

## Version 4.0 – Privacy Monitoring

- WebcamStatus
- MicrophoneStatus

Future releases will continue expanding OCMOSS with additional Windows monitoring capabilities.

---

# Disclaimer

OCMOSS retrieves system information using supported Windows interfaces. It does not bypass Windows security, exploit vulnerabilities, or perform unauthorized access.

---

# License

OCMOSS is licensed under the Apache License 2.0.

See the `LICENSE` file for complete license information.

---

# Author

**Shreyas Chimalwar**

GitHub Repository:
https://github.com/shreyaswar18-cell/OCMOSS

PyPI Package:
https://pypi.org/project/ocmoss/