import colorama
from colorama import Fore
import pyfiglet
import subprocess

colorama.init()

print(Fore.RED)
pyfiglet.print_figlet("Asylum")
print(Fore.GREEN)
print("             MAC Changer")
print(Fore.RESET)

def change_mac(interface, new_mac):
    print(Fore.GREEN + "[+] Changing MAC for interface " + interface + " to " + new_mac)
    print(Fore.RED)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

interface = input("Interface ==> ")
mac = input("MAC ==> ")

change_mac(interface, mac)
