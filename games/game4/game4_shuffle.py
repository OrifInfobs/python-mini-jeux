import random
from colorama import Fore, Style

def shuffle_list(lst):      
    shuffled_list = lst.copy()      # Make copy of list and store it as the "shuffled one" before actually randomly shuffling
    random.shuffle(shuffled_list)
    print("\nChoisissez l'intrus en entrant un numéro (1-4) :")
    for i, word in enumerate(shuffled_list, 1):
        print(f"{i}. {Fore.GREEN}{word}{Style.RESET_ALL}")  
    return shuffled_list
