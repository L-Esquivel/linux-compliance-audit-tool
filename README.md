# Linux Compliance Audit Tool (Python) 🛡️

## 🎯 Project Overview
This project is a technical laboratory focused on **Detection and Analysis** for IT Operations. It features a Python-based automation script designed to audit a Linux environment against industry-standard **CIS Benchmarks**.

The goal is to transition from manual security checks to a scalable, automated auditing process that identifies misconfigurations before they can be exploited.

## 🛠️ Tech Stack & Environment
*   **Language:** Python 3.x (utilizing `os` and `subprocess` libraries).
*   **Operating System:** Linux (Audited on a Beelink SER5 MAX 6800H).
*   **Framework:** Inspired by CIS (Center for Internet Security) Benchmarks.

## 🔍 Audit Scope (The Lab Exercise)
The tool focuses on five critical security controls:
1.  **SSH Configuration**: Disabling root login to prevent brute-force entry.
2.  **Filesystem Integrity**: Verifying critical permissions for `/etc/shadow` and `/etc/passwd`.
3.  **Service Hardening**: Identifying unnecessary active services that increase the attack surface.
4.  **Password Policy**: Auditing hashing algorithms and expiration settings.
5.  **User Privileges**: Detecting unauthorized accounts with UID 0 (Root privileges).

## 📋 The Iterative Process
Following a structured **Cybersecurity Recluitment** approach, this lab followed these stages:
1.  **Benchmarking**: Selecting high-impact controls based on industry standards.
2.  **Scripting**: Developing a Python tool to automate the "Detection" phase.
3.  **Analysis**: Transforming raw script output into a professional **Audit Report**.

## 🚀 How it Works
The script executes system commands to query the OS state, compares them against "Hardened" security standards, and flags any discrepancies as a **Security Gap**.


## 📈 Service Roadmap & Commercial Vision
This tool is the foundation for a specialized cybersecurity service suite tailored for Small and Medium Enterprises (SMEs) and VIP Digital Hygiene.

*   **Phase 1 (Current):** Automated Hardening & Compliance Auditing for Linux Infrastructure.
*   **Phase 2 (Q3 2026):** Executive Digital Hygiene Audits (MFA, OSINT Leak Detection).
*   **Phase 3 (Q4 2026):** Digital Evidence Preservation & First Responder Consulting, leveraging Criminology expertise.

---
*This repository is part of a specialized portfolio in IT Operations and Cybersecurity, demonstrating the ability to build custom security tooling.*
