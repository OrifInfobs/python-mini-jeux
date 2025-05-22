import colorama;
from colorama import Fore, Back, Style
colorama.init(autoreset=True) 
from colorama import init   # https://pypi.org/project/colorama/ pour plus d'infos sur les couleurs et comment les utiliser
init(autoreset=True)        # Automatically reset colors after each print as to not affect other prints
init(convert=None)          # For Windows compatibility