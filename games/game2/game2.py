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
    print("1. Facile (2 lettres révélées)")
    print("2. Moyen (1 lettre révélée)")
    print("3. Difficile (aucune lettre révélée)")
    difficulty = input("Entrez le numéro de la difficulté (1, 2 ou 3) : ").strip()
    # Validate difficulty input
    while difficulty not in ["1", "2", "3"]:
        print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
        difficulty = input("Entrez le numéro de la difficulté (1, 2 ou 3) : ").strip()
    secret_word = normalize(random.choice(wordle))  # Normalize the secret word
    attempts = 6
    has_won = False

    # Reveal letters based on difficulty
    if difficulty == "1":
        print(f"Le mot secret a été choisi. Voici un indice : les deux premières lettres sont '{secret_word[:2]}'.")
    elif difficulty == "2":
        print(f"Le mot secret a été choisi. Voici un indice : la première lettre est '{secret_word[0]}'.")
    else:
        print("Le mot secret a été choisi. Aucun indice n'est donné.")

    print("Vous avez à présent 6 essais pour le deviner.")

    # Attempt counter and word check loop
    while attempts > 0:
        #print(f"Mot secret (debug): {secret_word}")  # Debug word reveal
        word = normalize(input("Entrez un mot de 5 lettres : ").strip())  # Normalize user input
        if len(word) == 5:
            result = check_letters(word, secret_word)
            print(f"Résultat de l'essai: {result}")
            if word == secret_word:
                print("Vous avez deviné le mot secret!")
                has_won = True
                break
            attempts -= 1
        else:
            print("Mot invalide. Veuillez entrer un mot de 5 lettres.")

    if not has_won:
        print(f"Dommage! Vous avez perdu en raison d'avoir épuisé vos essais. Le mot secret était : {secret_word}")

    return has_won
# Function to check letters in the word + their positions + occurrences. God please don't modify this.
def check_letters(word, secret_word):
    secret_counter = {char: secret_word.count(char) for char in set(secret_word)}
    seen_counter = {char: 0 for char in set(secret_word)}
    result = []
    for i in range(len(word)):
        if word[i] == secret_word[i]:
            result.append("✔")
            seen_counter[word[i]] += 1
        elif word[i] in secret_word and seen_counter[word[i]] < secret_counter[word[i]]:
            result.append("➕")
            seen_counter[word[i]] += 1
        else:
            result.append("❌")
    return "".join(result)
# Main game function and boot to game manager
def play():
    while True:
        Clear()
        print("""
        \nBienvenue dans le jeu Wordle!
        Il faut deviner un mot secret de 5 lettres parmi une liste en 6 essais. Ces mots sont choisis aléatoirement et
        sont toujours des mots du dictionnaire valides.
        "✔" = lettre correcte et bien placée (présente dans le mot et à la bonne position)
        "❌" = Lettre incorrecte (non présente dans le mot)
        "➕" = lettre correcte mais mal placée (présente dans le mot mais pas à la bonne position)
        """)
        return check_word()
