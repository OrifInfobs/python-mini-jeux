"""
Initialize the random words game (Mots Aléatoires).
"""
from .game2_difficulty_selection import difficulty_selection
import random
from .game2_mots_aleatoires import wordle
from utils.normalize import normalize
from utils.colorama import Fore, Style


def initialize_game():
    """
    Initialize the game by selecting a difficulty level and defining a secret
    word.
    Returns:
        tuple: (original_word, secret_word)
    """
    difficulty = difficulty_selection()
    original_word = random.choice(wordle)
    secret_word = normalize(original_word)

    if difficulty == "1":
        print(
            f"\nLe mot secret a été choisi. Voici un indice : "
            f"les deux premières lettres sont "
            f"'{Fore.GREEN}{secret_word[:2]}{Style.RESET_ALL}'."
        )
    elif difficulty == "2":
        print(
            f"\nLe mot secret a été choisi. Voici un indice : "
            f"la première lettre est "
            f"'{Fore.GREEN}{secret_word[0]}{Style.RESET_ALL}'."
        )
    else:
        print("\nLe mot secret a été choisi. Aucun indice n'est donné.")
    print("\nVous avez à présent 6 essais pour le deviner.")
    return original_word, secret_word
