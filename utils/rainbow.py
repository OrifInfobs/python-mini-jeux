from colorama import Fore, Style
def rainbow_text(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]        # List of colors to cycle through
    result = "" 
    for i, char in enumerate(text):                     # Iterate over each character in the text
        result += colors[i % len(colors)] + char        # Assign a color to each character based on its index
    return result + Style.RESET_ALL