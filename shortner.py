import pyshorteners
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.YELLOW)
print("             _                  ")
print(" __ __ _____| |__ ___ _ __  ___ ")
print(" \ V  V / -_) / _/ _ \ '  \/ -_)")
print("  \_/\_/\___|_\__\___/_|_|_\___|")
print(Style.RESET_ALL)
print("\n")

print(Fore.GREEN)
link = input("---> Enter the link to shorten :\n")
print(Style.RESET_ALL)

shortener=pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(Fore.RED)
print("---> shortening.....")
print(Style.RESET_ALL)

print("---> Link 👉 " + Back.CYAN + x + Style.RESET_ALL)

print("\n")

print("---> Coded By " + Back.MAGENTA + "Swarnim Bandekar" + Style.RESET_ALL)