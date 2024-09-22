# Scapy Port Enumeration and Exploitation Tool

## Overview

`scapy-port-enum.py` is a versatile Python tool built with Scapy for penetration testers. It allows for scanning and basic exploitation of the most commonly hosted services on a target machine. The tool focuses on detecting open ports and associated services like FTP, SSH, DNS, HTTP, SMB, and HTTPS, providing a valuable resource for network security assessments.

## Features

- **Port Scanning**: Scans for commonly used service ports (21, 22, 25, 53, 80, 135, 139, 443).
- **Service-Specific Exploits**: Perform basic exploitation attempts on detected open service ports.
  - FTP Exploit (Port 21)
  - SSH Exploit (Port 22)
  - SMTP Exploit (Port 25)
  - DNS Exploit (Port 53)
  - HTTP Exploit (Port 80)
  - SMB Exploit (Ports 135, 139)
  - HTTPS Exploit (Port 443)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BoyEasyer/scapy-port-enum.git
   cd scapy-port-enum
   ```

2. **Install dependencies**:
   This tool utilizes Scapy for packet crafting. Install Scapy using:
   ```bash
   pip install scapy
   ```

3. **Make the script executable**:
   ```bash
   chmod +x scapy-port-enum.py
   ```

## Usage

To run the tool, use the following command:

```bash
./scapy-port-enum.py
```

### Main Menu Options:

1. **Scan Common Service Ports**: 
   Scans the target IP for commonly hosted service ports (21, 22, 25, 53, 80, 135, 139, 443).
   
2. **Exploit FTP (Port 21)**:
   Tests FTP vulnerabilities on the target (e.g., brute force or directory traversal).
   
3. **Exploit SSH (Port 22)**:
   Tests SSH vulnerabilities like brute force attacks.
   
4. **Exploit SMTP (Port 25)**:
   Tests SMTP vulnerabilities such as open relay and spoofing.
   
5. **Exploit DNS (Port 53)**:
   Tests DNS for vulnerabilities such as DNS cache poisoning or zone transfers.
   
6. **Exploit HTTP (Port 80)**:
   Tests HTTP for vulnerabilities such as SQLi, XSS, or LFI/RFI.
   
7. **Exploit SMB (Ports 135, 139)**:
   Tests SMB for vulnerabilities like EternalBlue or SMB enumeration.
   
8. **Exploit HTTPS (Port 443)**:
   Tests HTTPS for SSL/TLS vulnerabilities (e.g., Heartbleed).

### Example Usage:

1. To scan a target for common service ports:
   ```bash
   ./scapy-port-enum.py
   ```

   Choose option 1, and enter the target IP address when prompted.

2. To attempt an FTP exploit on a target:
   - Select option `2` after launching the script.
   - Enter the target IP address.

## Requirements

- Python 3.x
- Scapy library

Install dependencies using:

```bash
pip install scapy
```

## Supported Services and Ports

- **FTP**: Port 21
- **SSH**: Port 22
- **SMTP**: Port 25
- **DNS**: Port 53
- **HTTP**: Port 80
- **HTTPS**: Port 443
- **SMB**: Ports 135, 139

## License

This tool is open-source and available under the MIT License. Feel free to modify and distribute it as you like.
