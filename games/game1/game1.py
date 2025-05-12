import random

# Logique de cette fonction à remplacer par le jeux choisi
def play():

    print("\n")
    tries = 5
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    n3 = random.randint(0, 9)
    n4 = random.randint(0, 9)
    n5 = random.randint(0, 9)
    n6 = random.randint(0, 9)
    code = int(str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6))
    
    essai = input("Il vous reste " + str(tries) + " essais pour trouver le code à 6 chiffres. Veuillez sélectionner votre essai : "  )

    digit = [int(digit) for digit in str(essai)]

    if essai == digit:
        print("Correct ! Vous avez deviné le bon nombre.")
        return True
    else:
        print(f"Vous avez perdu ! Le code était {code}.")
        return False