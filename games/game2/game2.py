import random
import os
import unicodedata
from .mots_aleatoires import wordle

# Clear console function
Clear = lambda: os.system("cls")

# Function to check the word
def check_word():
    secret_word = random.choice(wordle)
    attempts = 6
    has_won = False
    print("Le mot secret a été choisi. Vous avez à présent 6 essais pour le deviner.")

    def normalize(input_word):
        return ''.join(
            c for c in unicodedata.normalize('NFD', input_word)
            if unicodedata.category(c) != 'Mn'
        ).lower()
    
    while attempts > 0:
        #print(f"Mot secret (debug): {secret_word}") #Debug word reveal
        word = input("Entrez un mot de 5 lettres : ").strip()
        word = normalize(word)
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
# Function to check letters in the word + their positions + occurrences. This was hell to write.
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
# Main game function
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
