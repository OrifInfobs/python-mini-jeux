import random
import os

# Mastermind numérique

def play():
    clear = lambda: os.system('cls')
    clear()
    print("\n")
    tries = 5
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    n3 = random.randint(0, 9)
    n4 = random.randint(0, 9)
    n5 = random.randint(0, 9)
    n6 = random.randint(0, 9)
    code = [n1, n2, n3, n4, n5, n6]
    print("Bienvenue dans le jeu Mastermind !")
    print("============================================================")
    print("""
        Vous devez deviner un code à 6 chiffres.
        Vous avez 5 essais pour le trouver.
        À chaque essai, vous recevrez des indices sur votre réponse.
        """)
    print("============================================================")
    while tries > 0:
        essai = input(f"Il vous reste {tries} essais pour trouver le code. Veuillez sélectionner votre essai : ")
        
        if len(essai) != 6 or not essai.isdigit():
            print("Veuillez entrer un code valide à 6 chiffres.")
            continue
        
        guess = [int(digit) for digit in essai]
        
        if guess == code:
            print("Correct ! Vous avez deviné le bon nombre.")
            return True
        
        correct_position = sum(1 for i in range(6) if guess[i] == code[i])
        correct_digits = sum(min(guess.count(d), code.count(d)) for d in set(guess)) - correct_position
        
        print(f"Faux ! {correct_position} chiffre(s) correct(s) à la bonne position, {correct_digits} chiffre(s) correct(s) mais à la mauvaise position.")
        print("\n")
        tries -= 1

    print(f"Vous avez perdu ! Le code était {''.join(map(str, code))}.")
    return False
