
import sys

def kitty():
    from colorama import init
    init(strip=not sys.stdout.isatty())
    from termcolor import cprint 
    from pyfiglet import figlet_format

    cprint(figlet_format('MEOW!', font='starwars'),
       'green', attrs=['bold'])