from colorama import Fore , init
import colorama
import pyfiglet 
import subprocess
import argparse
import os
print(colorama.Fore.RED)
pyfiglet.print_figlet("Asylum")
print(colorama.Fore.GREEN)
print("             MAC Changer")

print(colorama.Fore.RESET)
def change_mac(interface, new_mac):
    print(colorama.Fore.GREEN+"[+]Changing MAC for interface " + interface + " to " + new_mac)
    print(colorama.Fore.RED)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


interface = input("interface==> ")
mac = input("MAC==>")

change_mac(interface, mac)
