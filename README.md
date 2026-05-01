# Linux Compliance Audit Tool

**Automated Cybersecurity Compliance Auditor for Linux Systems using Python**

Professional tool that audits Linux servers against **CIS Benchmarks**, detects security misconfigurations, and generates detailed compliance reports.

### 🎯 Objective
Automate security auditing and compliance checking on Linux infrastructure to quickly identify vulnerabilities and hardening opportunities, supporting Defensive Security and IT Operations teams.

### ✨ Key Features
- Automated evaluation of selected CIS Benchmark controls (Level 1)
- Checks file permissions, ownership, and critical system settings
- Service, port, and user account security validation
- Password policy and authentication auditing
- Professional HTML and TXT report generation
- Modular design for easy customization and extension

### 🛠️ Technologies
- Python 3.10+
- Bash scripting integration
- Linux command-line tools
- HTML report generation

### 🚀 How to Use

```bash
# Clone the repository
git clone https://github.com/L-Esquivel/linux-compliance-audit-tool.git
cd linux-compliance-audit-tool

# Run full audit
python3 main.py

# Generate HTML report
python3 main.py --report html

# Run with specific options
python3 main.py --help
---
*This repository is part of a specialized portfolio in IT Operations and Cybersecurity, demonstrating the ability to build custom security tooling.*
