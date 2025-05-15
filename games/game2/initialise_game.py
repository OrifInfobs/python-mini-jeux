from .difficulty_selection import difficulty_selection
import random
from .mots_aleatoires import wordle
from utils.normalize import normalize

def initialize_game(): # Initialize the game by selecting a difficulty level and defining a secret word.
    difficulty = difficulty_selection()
    original_word = random.choice(wordle)  # Randomly select a word from the list
    secret_word = normalize(original_word)  # Normalize the secret word for the game

    if difficulty == "1":  # Reveal letters based on difficulty
        print(f"\nLe mot secret a été choisi. Voici un indice : les deux premières lettres sont '{secret_word[:2]}'.")
    elif difficulty == "2":
        print(f"\nLe mot secret a été choisi. Voici un indice : la première lettre est '{secret_word[0]}'.")
    else:
        print("\nLe mot secret a été choisi. Aucun indice n'est donné.")
    
    print("\nVous avez à présent 6 essais pour le deviner.")
    return original_word, secret_word