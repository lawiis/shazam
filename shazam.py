#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SHAZAM TOOLS v4 - Terminal Multi Utility Toolkit
Author: Lawiis
GitHub: github.com/lawiis
License: MIT
"""

import os
import sys
import socket
import hashlib
import base64
import subprocess
import platform
from datetime import datetime

# Third party imports
try:
    import requests
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    print("\n[!] Install dependencies first!")
    print("[!] pip install colorama requests\n")
    sys.exit(1)

# ==================== CONFIG ====================
VERSION = "4.0"
AUTHOR = "Lawiis"
GITHUB = "github.com/lawiis"
CLEAR_CMD = "cls" if platform.system() == "Windows" else "clear"

# ==================== UTILITIES ====================
def clear_screen():
    """Clear terminal screen"""
    os.system(CLEAR_CMD)

def print_banner():
    """Display banner with ASCII border"""
    banner = f"""
{Fore.CYAN}+------------------------------------------------------+
{Fore.CYAN}|{Fore.YELLOW}  ███████╗██╗  ██╗ █████╗ ███████╗ █████╗ ███╗   ███╗{Fore.CYAN} |
{Fore.CYAN}|{Fore.YELLOW}  ██╔════╝██║  ██║██╔══██╗╚══███╔╝██╔══██╗████╗ ████║{Fore.CYAN} |
{Fore.CYAN}|{Fore.YELLOW}  ███████╗███████║███████║  ███╔╝ ███████║██╔████╔██║{Fore.CYAN} |
{Fore.CYAN}|{Fore.YELLOW}  ╚════██║██╔══██║██╔══██║ ███╔╝  ██╔══██║██║╚██╔╝██║{Fore.CYAN} |
{Fore.CYAN}|{Fore.YELLOW}  ███████║██║  ██║██║  ██║███████╗██║  ██║██║ ╚═╝ ██║{Fore.CYAN} |
{Fore.CYAN}|{Fore.YELLOW}  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝{Fore.CYAN} |
{Fore.CYAN}+------------------------------------------------------+
{Fore.CYAN}|{Fore.GREEN}           SHAZAM TOOLS v{VERSION} - by {AUTHOR}{Fore.CYAN}              |
{Fore.CYAN}|{Fore.MAGENTA}            Terminal Multi Utility Toolkit{Fore.CYAN}            |
{Fore.CYAN}|{Fore.WHITE}              GitHub: {Fore.CYAN}{GITHUB}{Fore.CYAN}               |
{Fore.CYAN}+------------------------------------------------------+{Style.RESET_ALL}
"""
    print(banner)

def loading_animation(text="Loading"):
    """Simple loading animation"""
    for i in range(4):
        print(f"\r{Fore.YELLOW}{text}{'.' * i}{Style.RESET_ALL}", end="")
        import time
        time.sleep(0.3)
    print()

def print_menu():
    """Display main menu with ASCII border"""
    menu = f"""
{Fore.CYAN}═══════════════════════════════════════════════════════════
{Fore.YELLOW}                        MAIN MENU
{Fore.CYAN}═══════════════════════════════════════════════════════════

{Fore.GREEN}[1]{Fore.WHITE}  System Information
{Fore.GREEN}[2]{Fore.WHITE}  Public IP Checker
{Fore.GREEN}[3]{Fore.WHITE}  Multi Port Scanner
{Fore.GREEN}[4]{Fore.WHITE}  Hash Generator (MD5/SHA1/SHA256)
{Fore.GREEN}[5]{Fore.WHITE}  Base64 Encoder/Decoder
{Fore.GREEN}[6]{Fore.WHITE}  XOR Encryption/Decryption
{Fore.GREEN}[7]{Fore.WHITE}  Clear Screen
{Fore.RED}[0]{Fore.WHITE}  Exit

{Fore.CYAN}───────────────────────────────────────────────────────────
{Fore.WHITE}GitHub: {Fore.CYAN}{GITHUB}{Fore.WHITE} | Star if you like this tool!
{Fore.CYAN}───────────────────────────────────────────────────────────
{Style.RESET_ALL}"""
    print(menu)

# ==================== FEATURES ====================
def system_info():
    """Display system information"""
    clear_screen()
    print(f"{Fore.CYAN}+------------------------------------------+")
    print(f"{Fore.CYAN}|{Fore.YELLOW}        SYSTEM INFORMATION{Fore.CYAN}             ")
    print(f"{Fore.CYAN}+------------------------------------------+{Style.RESET_ALL}\n")
    
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Architecture": platform.machine(),
        "Hostname": socket.gethostname(),
        "Processor": platform.processor(),
        "Python Version": platform.python_version(),
        "Current Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    for key, value in info.items():
        print(f"{Fore.GREEN}{key}:{Fore.WHITE} {value}")
    
    input(f"\n{Fore.YELLOW}[+] Press Enter to return to menu...{Style.RESET_ALL}")

def public_ip():
    """Check public IP"""
    clear_screen()
    print(f"{Fore.CYAN}+------------------------------------------+")
    print(f"{Fore.CYAN}|{Fore.YELLOW}        PUBLIC IP CHECKER{Fore.CYAN}              ")
    print(f"{Fore.CYAN}+------------------------------------------+{Style.RESET_ALL}\n")
    
    loading_animation("Fetching IP data")
    
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        ip_data = response.json()
        
        # Get location info (optional)
        try:
            location = requests.get(f'http://ip-api.com/json/{ip_data["ip"]}', timeout=5)
            loc_data = location.json()
            
            print(f"{Fore.GREEN}IP Address:{Fore.WHITE} {ip_data['ip']}")
            print(f"{Fore.GREEN}Country:{Fore.WHITE} {loc_data.get('country', 'N/A')}")
            print(f"{Fore.GREEN}Region:{Fore.WHITE} {loc_data.get('regionName', 'N/A')}")
            print(f"{Fore.GREEN}City:{Fore.WHITE} {loc_data.get('city', 'N/A')}")
            print(f"{Fore.GREEN}ISP:{Fore.WHITE} {loc_data.get('isp', 'N/A')}")
            print(f"{Fore.GREEN}Lat/Lon:{Fore.WHITE} {loc_data.get('lat', 'N/A')}, {loc_data.get('lon', 'N/A')}")
        except:
            print(f"{Fore.GREEN}IP Address:{Fore.WHITE} {ip_data['ip']}")
            print(f"{Fore.YELLOW}[!] Location info unavailable")
            
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[X] Failed to get public IP: {e}")
    
    input(f"\n{Fore.YELLOW}[+] Press Enter to return to menu...{Style.RESET_ALL}")

def port_scan():
    """Scan port range"""
    clear_screen()
    print(f"{Fore.CYAN}+------------------------------------------+")
    print(f"{Fore.CYAN}|{Fore.YELLOW}        MULTI PORT SCANNER{Fore.CYAN}              ")
    print(f"{Fore.CYAN}+------------------------------------------+{Style.RESET_ALL}\n")
    
    target = input(f"{Fore.GREEN}Target IP/Hostname{Fore.WHITE}: ")
    start_port = input(f"{Fore.GREEN}Start Port{Fore.WHITE} (default 1): ")
    end_port = input(f"{Fore.GREEN}End Port{Fore.WHITE} (default 1024): ")
    
    # Set default values
    start_port = int(start_port) if start_port else 1
    end_port = int(end_port) if end_port else 1024
    
    print(f"\n{Fore.YELLOW}[*] Scanning {target} from port {start_port} to {end_port}...\n")
    
    open_ports = []
    try:
        target_ip = socket.gethostbyname(target)
        print(f"{Fore.CYAN}[+] Target IP: {target_ip}{Style.RESET_ALL}\n")
        
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"{Fore.GREEN}[+] Port {port} is OPEN{Style.RESET_ALL}")
                open_ports.append(port)
            sock.close()
        
        if not open_ports:
            print(f"{Fore.RED}[X] No open ports found{Style.RESET_ALL}")
            
    except socket.gaierror:
        print(f"{Fore.RED}[X] Invalid hostname{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Scan cancelled{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[X] Error: {e}{Style.RESET_ALL}")
    
    input(f"\n{Fore.YELLOW}[+] Press Enter to return to menu...{Style.RESET_ALL}")

def hash_generator():
    """Generate hash from text"""
    clear_screen()
    print(f"{Fore.CYAN}+------------------------------------------+")
    print(f"{Fore.CYAN}|{Fore.YELLOW}        HASH GENERATOR{Fore.CYAN}                 ")
    print(f"{Fore.CYAN}+------------------------------------------+{Style.RESET_ALL}\n")
    
    text = input(f"{Fore.GREEN}Input text{Fore.WHITE}: ")
    
    if not text:
        print(f"{Fore.RED}[X] Text cannot be empty!{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.CYAN}═══════════════ RESULTS ═══════════════{Style.RESET_ALL}\n")
        
        # MD5
        md5_hash = hashlib.md5(text.encode()).hexdigest()
        print(f"{Fore.GREEN}MD5:{Fore.WHITE}    {md5_hash}")
        
        # SHA1
        sha1_hash = hashlib.sha1(text.encode()).hexdigest()
        print(f"{Fore.GREEN}SHA1:{Fore.WHITE}   {sha1_hash}")
        
        # SHA256
        sha256_hash = hashlib.sha256(text.encode()).hexdigest()
        print(f"{Fore.GREEN}SHA256:{Fore.WHITE} {sha256_hash}")
    
    input(f"\n{Fore.YELLOW}[+] Press Enter to return to menu...{Style.RESET_ALL}")

def base64_tools():
    """Base64 encoder/decoder"""
    clear_screen()
    print(f"{Fore.CYAN}+------------------------------------------+")
    print(f"{Fore.CYAN}|{Fore.YELLOW}     BASE64 ENCODER/DECODER{Fore.CYAN}          ")
    print(f"{Fore.CYAN}+------------------------------------------+{Style.RESET_ALL}\n")
    
    print(f"{Fore.GREEN}[1]{Fore.WHITE} Encode")
    print(f"{Fore.GREEN}[2]{Fore.WHITE} Decode")
    
    choice = input(f"\n{Fore.GREEN}Choose{Fore.WHITE} [1/2]: ")
    text = input(f"{Fore.GREEN}Input text{Fore.WHITE}: ")
    
    if not text:
        print(f"{Fore.RED}[X] Text cannot be empty!{Style.RESET_ALL}")
    else:
        try:
            if choice == "1":
                encoded = base64.b64encode(text.encode()).decode()
                print(f"\n{Fore.CYAN}═══════════ ENCODE RESULT ═══════════{Style.RESET_ALL}\n")
                print(f"{Fore.GREEN}Result:{Fore.WHITE} {encoded}")
            elif choice == "2":
                decoded = base64.b64decode(text.encode()).decode()
                print(f"\n{Fore.CYAN}═══════════ DECODE RESULT ═══════════{Style.RESET_ALL}\n")
                print(f"{Fore.GREEN}Result:{Fore.WHITE} {decoded}")
            else:
                print(f"{Fore.RED}[X] Invalid choice!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[X] Error: Make sure input is valid for decode!{Style.RESET_ALL}")
    
    input(f"\n{Fore.YELLOW}[+] Press Enter to return to menu...{Style.RESET_ALL}")

def xor_cipher():
    """XOR encryption/decryption"""
    clear_screen()
    print(f"{Fore.CYAN}+------------------------------------------+")
    print(f"{Fore.CYAN}|{Fore.YELLOW}    XOR ENCRYPTION/DECRYPTION{Fore.CYAN}        ")
    print(f"{Fore.CYAN}+------------------------------------------+{Style.RESET_ALL}\n")
    
    print(f"{Fore.GREEN}[1]{Fore.WHITE} Encrypt")
    print(f"{Fore.GREEN}[2]{Fore.WHITE} Decrypt")
    
    choice = input(f"\n{Fore.GREEN}Choose{Fore.WHITE} [1/2]: ")
    text = input(f"{Fore.GREEN}Input text{Fore.WHITE}: ")
    key = input(f"{Fore.GREEN}Input key{Fore.WHITE}: ")
    
    if not text or not key:
        print(f"{Fore.RED}[X] Text and key cannot be empty!{Style.RESET_ALL}")
    else:
        # XOR operation
        result = ""
        key_length = len(key)
        for i, char in enumerate(text):
            result += chr(ord(char) ^ ord(key[i % key_length]))
        
        # Convert to hex for display
        result_hex = result.encode().hex()
        
        print(f"\n{Fore.CYAN}════════════════ RESULTS ════════════════{Style.RESET_ALL}\n")
        print(f"{Fore.GREEN}Result (hex):{Fore.WHITE} {result_hex}")
        print(f"{Fore.GREEN}Result (raw):{Fore.WHITE} {repr(result)}")
    
    input(f"\n{Fore.YELLOW}[+] Press Enter to return to menu...{Style.RESET_ALL}")

# ==================== MAIN ====================
def main():
    """Main program loop"""
    try:
        while True:
            clear_screen()
            print_banner()
            print_menu()
            
            choice = input(f"{Fore.GREEN}Choose menu{Fore.WHITE} [0-7]: {Style.RESET_ALL}")
            
            if choice == "1":
                system_info()
            elif choice == "2":
                public_ip()
            elif choice == "3":
                port_scan()
            elif choice == "4":
                hash_generator()
            elif choice == "5":
                base64_tools()
            elif choice == "6":
                xor_cipher()
            elif choice == "7":
                clear_screen()
                print_banner()
                print_menu()
            elif choice == "0":
                print(f"\n{Fore.YELLOW}Thanks for using Shazam Tools! Goodbye~{Style.RESET_ALL}")
                sys.exit(0)
            else:
                print(f"\n{Fore.RED}[X] Invalid choice, try again!{Style.RESET_ALL}")
                import time
                time.sleep(1)
                
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}[!] Program terminated. Goodbye!{Style.RESET_ALL}")
        sys.exit(0)

if __name__ == "__main__":
    main()
