import os
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# ASCII Art
ascii_art = f"""
{Fore.RED}__________        __    __________        .__    .___    _____   __          
{Fore.YELLOW}\______   \ _____/  |_  \______   \_____  |__| __| _/   /  _  \_/  |____  ___
{Fore.GREEN} |    |  _//  _ \   __\  |       _/\__  \ |  |/ __ |   /  /_\  \   __\  \/  /
{Fore.CYAN} |    |   (  <_> )  |    |    |   \ / __ \|  / /_/ |  /    |    \  |  >    < 
{Fore.BLUE} |______  /\____/|__|    |____|_  /(____  /__\____ |  \____|__  /__| /__/\_ \\
{Fore.MAGENTA}        \/                    \/      \/        \/          \/           \/

{Fore.LIGHTMAGENTA_EX}[ + ] Cliquez sur entrez pour lancer le programme :
"""

print(ascii_art)
input()

# Clear terminal and launch bot.py
os.system('cls' if os.name == 'nt' else 'clear')
os.system('python bot.py')
