#!/usr/bin/env python3

# Importing necessary modules
from scapy.all import *
import argparse

# Commonly hosted service ports
common_ports = [21, 22, 25, 53, 80, 135, 139, 443]

# Function to scan commonly hosted services
def scan_common_ports(target_ip):
    print(f"\n[+] Scanning Common Service Ports on {target_ip}...\n")
    open_ports = []
    
    # Sending SYN packet for each port
    for port in common_ports:
        syn_pkt = IP(dst=target_ip) / TCP(dport=port, flags='S')
        response = sr1(syn_pkt, timeout=1, verbose=0)
        
        # Checking if SYN-ACK response is received (indicating an open port)
        if response and response.haslayer(TCP) and response[TCP].flags == 'SA':
            print(f"[+] Port {port} is open")
            open_ports.append(port)
        else:
            print(f"[-] Port {port} is closed")
    
    print("\n[+] Scan complete. Open ports:", open_ports)
    return open_ports

# Function for FTP Exploit on Port 21
def exploit_ftp(target_ip):
    print(f"\n[+] Starting FTP Exploit on {target_ip}:21")
    ftp_syn = IP(dst=target_ip) / TCP(dport=21, flags='S')
    response = sr1(ftp_syn, timeout=2, verbose=0)
    
    if response and response.haslayer(TCP) and response[TCP].flags == 'SA':
        print(f"[+] Port 21 is open! Service: FTP")
        print("[*] You can attempt brute-force or directory traversal attacks on FTP.")
    else:
        print("[-] Port 21 seems closed.")

# Function for SSH Exploit on Port 22
def exploit_ssh(target_ip):
    print(f"\n[+] Starting SSH Exploit on {target_ip}:22")
    ssh_syn = IP(dst=target_ip) / TCP(dport=22, flags='S')
    response = sr1(ssh_syn, timeout=2, verbose=0)
    
    if response and response.haslayer(TCP) and response[TCP].flags == 'SA':
        print(f"[+] Port 22 is open! Service: SSH")
        print("[*] Consider trying brute-force attacks or known SSH vulnerabilities.")
    else:
        print("[-] Port 22 seems closed.")

# Function for SMTP Exploit on Port 25
def exploit_smtp(target_ip):
    print(f"\n[+] Starting SMTP Exploit on {target_ip}:25")
    smtp_syn = IP(dst=target_ip) / TCP(dport=25, flags='S')
    response = sr1(smtp_syn, timeout=2, verbose=0)
    
    if response and response.haslayer(TCP) and response[TCP].flags == 'SA':
        print(f"[+] Port 25 is open! Service: SMTP")
        print("[*] Consider checking for open relay or spoofing vulnerabilities.")
    else:
        print("[-] Port 25 seems closed.")

# Function for DNS Exploit on Port 53
def exploit_dns(target_ip):
    print(f"\n[+] Starting DNS Exploit on {target_ip}:53")
    dns_request = IP(dst=target_ip) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="example.com"))
    response = sr1(dns_request, timeout=2, verbose=0)
    
    if response and response.haslayer(DNS):
        print(f"[+] Port 53 is open! Service: DNS")
        print("[*] Check for DNS cache poisoning or zone transfer vulnerabilities.")
    else:
        print("[-] Port 53 seems closed.")

# Function for HTTP Exploit on Port 80
def exploit_http(target_ip):
    print(f"\n[+] Starting HTTP Exploit on {target_ip}:80")
    http_syn = IP(dst=target_ip) / TCP(dport=80, flags='S')
    response = sr1(http_syn, timeout=2, verbose=0)
    
    if response and response.haslayer(TCP) and response[TCP].flags == 'SA':
        print(f"[+] Port 80 is open! Service: HTTP")
        print("[*] Consider testing for SQLi, XSS, LFI/RFI, or other common web vulnerabilities.")
    else:
        print("[-] Port 80 seems closed.")

# Function for HTTPS Exploit on Port 443
def exploit_https(target_ip):
    print(f"\n[+] Starting HTTPS Exploit on {target_ip}:443")
    https_syn = IP(dst=target_ip) / TCP(dport=443, flags='S')
    response = sr1(https_syn, timeout=2, verbose=0)
    
    if response and response.haslayer(TCP) and response[TCP].flags == 'SA':
        print(f"[+] Port 443 is open! Service: HTTPS")
        print("[*] Consider testing for SSL/TLS vulnerabilities (Heartbleed, weak ciphers).")
    else:
        print("[-] Port 443 seems closed.")

# Function for SMB Exploit on Ports 135 and 139
def exploit_smb(target_ip):
    print(f"\n[+] Starting SMB Exploit on {target_ip}:135 and 139")
    smb_syn_135 = IP(dst=target_ip) / TCP(dport=135, flags='S')
    smb_syn_139 = IP(dst=target_ip) / TCP(dport=139, flags='S')
    
    response_135 = sr1(smb_syn_135, timeout=2, verbose=0)
    response_139 = sr1(smb_syn_139, timeout=2, verbose=0)
    
    if response_135 and response_135.haslayer(TCP) and response_135[TCP].flags == 'SA':
        print(f"[+] Port 135 is open! Service: SMB (RPC)")
        print("[*] Consider checking for SMB vulnerabilities (EternalBlue, SMB Relay).")
    else:
        print("[-] Port 135 seems closed.")
    
    if response_139 and response_139.haslayer(TCP) and response_139[TCP].flags == 'SA':
        print(f"[+] Port 139 is open! Service: SMB (NetBIOS)")
        print("[*] Check for NetBIOS-related vulnerabilities or SMB enumeration.")
    else:
        print("[-] Port 139 seems closed.")

# Main menu for tool interaction
def main():
    print("\n========== Scapy Exploitation Tool (Common Services) ==========\n")
    print("[1] Scan Common Service Ports")
    print("[2] Exploit FTP (Port 21)")
    print("[3] Exploit SSH (Port 22)")
    print("[4] Exploit SMTP (Port 25)")
    print("[5] Exploit DNS (Port 53)")
    print("[6] Exploit HTTP (Port 80)")
    print("[7] Exploit SMB (Ports 135, 139)")
    print("[8] Exploit HTTPS (Port 443)")
    print("[0] Exit")
    
    choice = input("\nEnter your choice: ")

    if choice == '1':
        target_ip = input("Enter target IP address: ")
        open_ports = scan_common_ports(target_ip)
        print("\nOpen ports:", open_ports)
    elif choice == '2':
        target_ip = input("Enter target IP address: ")
        exploit_ftp(target_ip)
    elif choice == '3':
        target_ip = input("Enter target IP address: ")
        exploit_ssh(target_ip)
    elif choice == '4':
        target_ip = input("Enter target IP address: ")
        exploit_smtp(target_ip)
    elif choice == '5':
        target_ip = input("Enter target IP address: ")
        exploit_dns(target_ip)
    elif choice == '6':
        target_ip = input("Enter target IP address: ")
        exploit_http(target_ip)
    elif choice == '7':
        target_ip = input("Enter target IP address: ")
        exploit_smb(target_ip)
    elif choice == '8':
        target_ip = input("Enter target IP address: ")
        exploit_https(target_ip)
    elif choice == '0':
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid option! Please try again.")
        main()

if __name__ == '__main__':
    main()
