import random
from utils import get_integer_input

def play():
    """
    Mini-jeu : Deviner un nombre entre 1 et 5.
    Retourne True si le joueur devine, False sinon.
    """
    print("\n🎲 Bienvenue dans le mini-jeu : Devine le nombre !")
    number_to_guess = random.randint(1, 5)
    
    guess = get_integer_input("Devinez un nombre entre 1 et 5 : ", 1, 5)

    if guess == number_to_guess:
        print("🎉 Correct ! Vous avez deviné le bon nombre.")
        return True
    else:
        print(f"❌ Mauvais choix ! Le nombre était {number_to_guess}.")
        return False