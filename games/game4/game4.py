import random
import os
import unicodedata
from .liste_intrus import intrus

# Clear console function
def Clear():
    os.system("cls")

# Normalize input text (remove accents and convert to lowercase)
def normalize(input_text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', input_text.strip())
        if unicodedata.category(c) != 'Mn'
    ).lower()

# Function to randomly select a theme and an imposter word
def select_theme_and_imposter():
    theme = random.choice(list(intrus.keys()))
    normal_words, imposter_words = intrus[theme]
    # Normalize all words
    normal_words = [normalize(word) for word in normal_words]
    imposter_word = normalize(imposter_words[0])
    return theme, normal_words, imposter_word

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
def check_player_guess(imposter_word):
    player_guess = normalize(input("\nEntrez le mot intrus : ").strip())
    if player_guess == imposter_word:
        print("\nFélicitations ! Vous avez trouvé l'intrus 🎉")
        return True 
    else:
        print(f"\nDésolé, ce n'est pas le bon mot. L'intrus était : {imposter_word}")
        return False 

# Main game logic
def game():
    while True:
        # Select theme and imposter word
        theme, normal_words, imposter_word = select_theme_and_imposter()
        # Combine and shuffle words
        words_with_imposter = normal_words + [imposter_word]
        shuffled_words = shuffle_list(words_with_imposter)
        # Display theme and shuffled words
        display_theme_and_words(theme, shuffled_words)
        # Check player's guess
        if check_player_guess(imposter_word):
            return True
        else:
            return False
        
# Main game loop
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