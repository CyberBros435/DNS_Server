#!/usr/bin/env python3
import os
import sys
import socket
import platform
import subprocess
from colorama import Fore, Style, init

# Auto-reset colors after each print (fixes Windows color issues)
init(autoreset=True)

BANNER = f"""{Fore.MAGENTA}
:::::  ::    ::   ::::        ::::   :::::  :::::   ::      ::  :::::    :::::
::  :  :: .  ::   ::  .       ::  .  ::___  ::   :  ::     ::   ::___    ::   :
::  :  ::  . ::  .  ::        . ::   ::     :::::     :: ::     ::       :::::
:::::  ::   .::   ::::        ::::   :::::  ::   .      :       :::::    ::   .{Style.RESET_ALL}
"""

def get_platform():
    return platform.system().lower()  # 'windows', 'linux', 'darwin'

def run_dns_lookup(hostname):
    """Run nslookup cross-platform."""
    system = get_platform()

    try:
        if system == "windows":
            # nslookup exists natively on Windows
            result = subprocess.run(
                ["nslookup", hostname],
                capture_output=True, text=True
            )
        else:
            # Linux/macOS: prefer dig, fall back to nslookup, then socket
            if shutil_which("dig"):
                result = subprocess.run(
                    ["dig", "+short", hostname],
                    capture_output=True, text=True
                )
            elif shutil_which("nslookup"):
                result = subprocess.run(
                    ["nslookup", hostname],
                    capture_output=True, text=True
                )
            else:
                # Pure Python fallback using socket
                ip = socket.gethostbyname(hostname)
                print(f"{Fore.GREEN}  Resolved: {hostname} → {ip}{Style.RESET_ALL}")
                return ip

        output = result.stdout or result.stderr
        print(output)
        return output

    except socket.gaierror:
        print(f"{Fore.RED}  [!] Could not resolve hostname: {hostname}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}  [!] DNS tool not found. Trying Python socket...{Style.RESET_ALL}")
        try:
            ip = socket.gethostbyname(hostname)
            print(f"{Fore.GREEN}  Resolved: {hostname} → {ip}{Style.RESET_ALL}")
            return ip
        except socket.gaierror:
            print(f"{Fore.RED}  [!] Resolution failed for: {hostname}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}  [!] Error: {e}{Style.RESET_ALL}")

def shutil_which(cmd):
    """Check if a CLI command exists (cross-platform)."""
    import shutil
    return shutil.which(cmd) is not None

def clear_screen():
    if get_platform() == "windows":
        os.system("cls")
    else:
        os.system("clear")

class DNS:
    def __init__(self):
        print(BANNER)
        print(f"{Fore.CYAN}  Platform detected: {platform.system()} {platform.release()}{Style.RESET_ALL}\n")

    def dns_server(self):
        hostname = input(
            f"{Fore.BLUE}\n  [ + ] Enter hostname (e.g. google.com) or 'q' to exit: {Style.RESET_ALL}"
        ).strip()

        if hostname.lower() == "q":
            print(f"{Fore.GREEN}  Exiting...{Style.RESET_ALL}")
            return None, None

        if not hostname:
            print(f"{Fore.YELLOW}  [!] No hostname entered.{Style.RESET_ALL}")
            return None, None

        if hostname.replace(".", "").isdigit():
            print(f"{Fore.RED}  [!] That looks like an IP, not a hostname.{Style.RESET_ALL}")
            return None, hostname

        result = run_dns_lookup(hostname)
        return result, hostname

def main():
    o = DNS()
    while True:
        try:
            choice = input(
                f"{Fore.BLUE}\n  [ + ] Do you want to continue? (y/n): {Style.RESET_ALL}"
            ).strip().lower()

            if choice == "y":
                result, hostname = o.dns_server()
                if hostname is None:
                    break
            elif choice == "n":
                print(f"{Fore.GREEN}  Goodbye!{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}  [!] Invalid option. Enter 'y' or 'n'.{Style.RESET_ALL}")

        except KeyboardInterrupt:
            print(f"\n{Fore.GREEN}  Interrupted. Goodbye!{Style.RESET_ALL}")
            sys.exit(0)

if __name__ == "__main__":
    main()
