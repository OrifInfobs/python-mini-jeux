import random
import os
from .mots_aleatoires import wordle
import unicodedata

# Clear console function
Clear = lambda: os.system("cls")
# Enlève les accents et met en minuscule le mot entré par l'utilisateur
def normalize(input_text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', input_text)
        if unicodedata.category(c) != 'Mn'
    ).lower()
def check_word():
# Difficulty selection
    print("Choisissez une difficulté :")
    print("\n1. Facile (2 lettres révélées)")
    print("\n2. Moyen (1 lettre révélée)")
    print("\n3. Difficile (aucune lettre révélée)")
    difficulty = input("\nEntrez le numéro de la difficulté (1, 2 ou 3) : ").strip()
# Validate difficulty input
    while difficulty not in ["1", "2", "3"]:
        print("\nChoix invalide. Veuillez entrer 1, 2 ou 3.")
        difficulty = input("Entrez le numéro de la difficulté (1, 2 ou 3) : ").strip()
    print("============================================================")
 # Randomly select a word from the list
    original_word = random.choice(wordle)
# Normalize the secret word for the game
    secret_word = normalize(original_word)  
# Attempts counters and game state
    attempts = 6
    total_attempts = 0
    has_won = False
# Reveal letters based on difficulty
    if difficulty == "1":
        print(f"\nLe mot secret a été choisi. Voici un indice : les deux premières lettres sont '{secret_word[:2]}'.")
    elif difficulty == "2":
        print(f"\nLe mot secret a été choisi. Voici un indice : la première lettre est '{secret_word[0]}'.")
    else:
        print("\nLe mot secret a été choisi. Aucun indice n'est donné.")
    print("\nVous avez à présent 6 essais pour le deviner.")
# Attempt counter and word check loop
    while attempts > 0:

#       print(f"\nMot secret (debug): {original_word}")  # Debug word reveal

# Normalize user input
        word = normalize(input("\nEntrez un mot de 5 lettres : ").strip())
# Validate user input word length
        if len(word) == 5:
            # Compare the word with the secret word
            result = check_letters(word, secret_word)
# Display the result in a more readable format
            print("\n============================================================")
            print(f"🔍 Résultat de l'essai : {result}")
            print(f"💡 Mot entré : {word}")
            print(f"🔄 Essais restants : {attempts}")
            print("============================================================\n")
# If the word is correct, end the game
            if word == secret_word:
                print(f"🎉 Félicitations ! Vous avez deviné le mot secret '{secret_word}' en {total_attempts + 1} essais ! 🎉")
                has_won = True
                break
            attempts -= 1
            total_attempts += 1
        else:
            print("\n❌ Mot invalide. Veuillez entrer un mot de 5 lettres.")
# If the user has exhausted all attempts, reveal the secret word
    if not has_won:
        print("\n============================================================")
        print(f"Dommage ! Vous avez perdu. Le mot secret était : '{original_word}'.")
        print("============================================================")
    return has_won
# Function to check letters in the word + their positions + occurrences. 
# I had to modify this damn function from 85-91 since it was causing a bug. I don't know why yet but it was not counting the letters correctly.
def check_letters(word, secret_word):
    secret_counter = {char: secret_word.count(char) for char in set(secret_word)}
    seen_counter = {char: 0 for char in set(secret_word)}
    result = []
    for i in range(len(word)):
# Correct letter and position
        if word[i] == secret_word[i]:
            result.append("✔")
            seen_counter[word[i]] += 1
# Correct letter but wrong position
        elif word[i] in secret_word and seen_counter[word[i]] < secret_counter[word[i]]:
# Check if the letter has already been counted
# But IMBEDDED WITHIN the "correct position" function as to prioritize the correct position first so over time in a game it won't start making mistakes.
            if word.count(word[i]) <= secret_counter[word[i]]:
                result.append("➕")
                seen_counter[word[i]] += 1
# All occurrences already accounted for
            else:
                result.append("➖") 
# Letter not in the word
        else:
            result.append("❌")
    return "".join(result)
# Main game function and boot to game manager
def play():
    while True:
        Clear()
        print("""
============================================================
            🎉 BIENVENUE DANS LE MINI JEUX WORDLE 🎉
============================================================

Devinez un mot secret de 5 lettres parmi une liste en 6 essais.
Ces mots sont choisis aléatoirement et sont toujours des mots
du dictionnaire valides.

Voici les symboles que vous verrez dans les résultats de vos essais:

    ✔ = Lettre correcte et bien placée
    ❌ = Lettre incorrecte (non présente dans le mot)
    ➕ = Lettre correcte mais mal placée
    ➖ = Lettre correcte mais toutes les occurrences ont déjà été comptées

    Bonne chance! 
============================================================
""")
        return check_word()