from utils.colorama import Fore, Style

def display_theme_and_words(theme, shuffled_words):
    print(f"\n{Fore.CYAN}Thème : {theme}{Style.RESET_ALL}\n")
    for i, word in enumerate(shuffled_words, 1):
        print(f"{Fore.GREEN}{Style.BRIGHT}{i}.{Style.RESET_ALL} {word}")