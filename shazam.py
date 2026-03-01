import os
import socket
import hashlib
import platform
import shutil
import requests
import base64
import time
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# ==========================
# CLEAR SCREEN
# ==========================

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ==========================
# BANNER
# ==========================

def banner():
    print(Fore.RED + r"""
███████╗██╗  ██╗ █████╗ ███████╗ █████╗ ███╗   ███╗
██╔════╝██║  ██║██╔══██╗╚══███╔╝██╔══██╗████╗ ████║
███████╗███████║███████║  ███╔╝ ███████║██╔████╔██║
╚════██║██╔══██║██╔══██║ ███╔╝  ██╔══██║██║╚██╔╝██║
███████║██║  ██║██║  ██║███████╗██║  ██║██║ ╚═╝ ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
        made by lawis "github.com/lawiis"
""")

# ==========================
# SYSTEM INFO
# ==========================

def system_info():
    print(Fore.MAGENTA + "\n[ SYSTEM INFO ]")
    print("OS:", platform.system(), platform.release())
    print("Arch:", platform.machine())
    print("CPU:", platform.processor())
    total, used, free = shutil.disk_usage("/")
    print("Disk Total (GB):", round(total / (1024**3), 2))
    print("Disk Free (GB):", round(free / (1024**3), 2))
    print("Time:", datetime.now())

# ==========================
# PUBLIC IP
# ==========================

def public_ip():
    try:
        ip = requests.get("https://api.ipify.org", timeout=5).text
        print(Fore.GREEN + "\nPublic IP:", ip)
    except:
        print(Fore.RED + "Failed to fetch IP")

# ==========================
# PORT CHECK
# ==========================

def port_scan():
    try:
        host = input("Host: ")
        ports_input = input("Ports (comma separated): ")

        ports = [int(p.strip()) for p in ports_input.split(",")]

        print(Fore.YELLOW + "\nScanning...")
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                s.connect((host, port))
                print(Fore.GREEN + f"Port {port} OPEN")
            except:
                print(Fore.RED + f"Port {port} CLOSED")
            finally:
                s.close()

    except:
        print(Fore.RED + "Invalid port input!")

# ==========================
# HASH GENERATOR
# ==========================

def hash_generator():
    try:
        text = input("Text: ").encode()
        print("MD5:", hashlib.md5(text).hexdigest())
        print("SHA1:", hashlib.sha1(text).hexdigest())
        print("SHA256:", hashlib.sha256(text).hexdigest())
    except:
        print(Fore.RED + "Error generating hash")

# ==========================
# XOR FUNCTION
# ==========================

def xor_cipher(data, key):
    if not key:
        raise ValueError("Key cannot be empty")

    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

# ==========================
# ENCRYPT
# ==========================

def encrypt_menu():
    print("\n1. Base64 Encode")
    print("2. XOR Encrypt")
    choice = input("Select: ")

    try:
        if choice == "1":
            text = input("Text: ").encode()
            encoded = base64.b64encode(text).decode()
            print(Fore.GREEN + "Encoded:", encoded)

        elif choice == "2":
            text = input("Text: ")
            key = input("Key: ")

            encrypted = xor_cipher(text, key)
            encoded = base64.b64encode(encrypted.encode()).decode()

            print(Fore.GREEN + "Encrypted (Base64):", encoded)

        else:
            print(Fore.RED + "Invalid option")

    except:
        print(Fore.RED + "Encryption error!")

# ==========================
# DECRYPT
# ==========================

def decrypt_menu():
    print("\n1. Base64 Decode")
    print(f"2. XOR Decrypt {Style.BRIGHT}{Fore.RED}(use the correct key){Style.RESET_ALL}")
    choice = input("Select: ")

    try:
        if choice == "1":
            text = input("Encoded: ").encode()
            decoded = base64.b64decode(text).decode()
            print(Fore.GREEN + "Decoded:", decoded)

        elif choice == "2":
            text = input("Encrypted (Base64): ")
            key = input("Key: ")

            decoded_base = base64.b64decode(text).decode()
            decrypted = xor_cipher(decoded_base, key)

            print(Fore.GREEN + "Decrypted:", decrypted)

        else:
            print(Fore.RED + "Invalid option")

    except:
        print(Fore.RED + "❌ Invalid key or corrupted input!")

# ==========================
# MAIN
# ==========================

def main():
    banner()

    while True:
        print(Fore.CYAN + """
1. System Info
2. Public IP
3. Multi Port Check
4. Hash Generator
5. Encrypt
6. Decrypt
7. Exit
""")

        choice = input("Select: ")

        if choice == "1":
            system_info()
        elif choice == "2":
            public_ip()
        elif choice == "3":
            port_scan()
        elif choice == "4":
            hash_generator()
        elif choice == "5":
            encrypt_menu()
        elif choice == "6":
            decrypt_menu()
        elif choice == "7":
            print(Fore.YELLOW + "SHAZAM shutting down")
            break
        else:
            print(Fore.RED + "Invalid option")

        input("\nPress Enter...")
        os.system("cls" if os.name == "nt" else "clear")
        banner()

if __name__ == "__main__":
    try:
        clear()   # langsung clear saat start
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\nGood Byee")
        time.sleep(1)
        clear()
        exit()