from utils.colorama import Fore, Style

def display_theme_and_words(theme, shuffled_words):
    print(f"\n{Fore.CYAN}Thème : {theme}{Style.RESET_ALL}\n") # Display the theme in cyan
    for i, word in enumerate(shuffled_words, 1):              # Enumerate the shuffled words starting from 1 
        print(f"{Fore.GREEN}{Style.BRIGHT}{i}.{Style.RESET_ALL} {word}")    # Display each word in bright green and bold