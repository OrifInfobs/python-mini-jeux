import random
import os
from utils.normalize import normalize
from .liste_intrus import intrus

# Clear console function
def Clear():
    os.system("cls")
# Function to randomly select a theme and an imposter word
def select_theme_and_imposter():
# Select 5 random themes from the available keys in the `intrus` dictionary
    available_themes = random.sample(list(intrus.keys()), 5)
    print("Choisissez un thème parmi les options suivantes :")
    for i, theme in enumerate(available_themes, start=1):
        print(f"{i}. {theme}")
    while True:
        try:
# Get the player's choice
            choice = int(input("\nEntrez le numéro correspondant à votre choix : ").strip())
            if 1 <= choice <= len(available_themes):
                selected_theme = available_themes[choice - 1]
                break
            else:
                print("Veuillez entrer un numéro valide entre 1 et 5.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro.")
# Retrieve the normal and imposter words for the selected theme
    normal_words, imposter_words = intrus[selected_theme]
# Normalize all words
    normal_words = [normalize(word) for word in normal_words]
    imposter_word = normalize(imposter_words[0])
    return selected_theme, normal_words, imposter_word
# Shuffle a list and return the shuffled list
def shuffle_list(lst):
    shuffled_list = lst.copy()
    random.shuffle(shuffled_list)
    return shuffled_list
# Display the theme and shuffled words
def display_theme_and_words(theme, shuffled_words):
    print(f"Thème : {theme}")
    print("\n")
    for word in shuffled_words:
        print(f"- {word}")
# Function to check the player's guess against the imposter word
def check_player_guess(imposter_word, shuffled_words):
    print("\nChoisissez le mot intrus en entrant un numéro (1-4) :")
    for i, word in enumerate(shuffled_words, start=1):
        print(f"{i}. {word}")
    while True:
        try:
# Get player's choice as a number + error handling
            choice = int(input("\nEntrez le numéro correspondant à votre choix : ").strip())
            if 1 <= choice <= len(shuffled_words):
                selected_word = shuffled_words[choice - 1]
                break
            else:
                print("Veuillez entrer un numéro valide entre 1 et 4.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro.")

    if selected_word == imposter_word:
        print("\nFélicitations ! Vous avez trouvé l'intrus 🎉")
        return True
    else:
        print(f"\nDésolé, ce n'est pas le bon mot. L'intrus était : {imposter_word}")
        return False
# Main game logic
def game():
    global shuffled_words, theme, imposter_word, check_player_guess
    while True:
# Select theme and imposter word
        theme, normal_words, imposter_word = select_theme_and_imposter()
# Combine and shuffle words
        words_with_imposter = normal_words + [imposter_word]
        shuffled_words = shuffle_list(words_with_imposter)
# Check player's guess
        if check_player_guess(imposter_word, shuffled_words):
            return True
        else:
            return False
def play():
    while True:
        Clear()
        print("""
============================================================
🎉 BIENVENUE DANS LE MINI JEUX TROUVEZ L'INTRUS 🎉
============================================================

L'objectif est de trouver le mot intrus parmi les 4 qui seront listés. Vous devez trouver le mot secret en choisissant
parmi les 4 mots proposés. Ne vous souciez pas, les accents ou majuscules ne comptent pas.

Bonne chance! 
              
============================================================
        """)
        return game()