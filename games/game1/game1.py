import os
import random
from colorama import init, Fore

init(autoreset=True)

MAGIC_CODE = "1355"  # Code magique pour gagner instantanément


def clear_console():
    """Efface la console."""
    os.system('cls' if os.name == 'nt' else 'clear')


def play() -> bool:
    """
    le joueur doit deviner un code à 6 chiffres en 5 essais.
    Retourne True si le joueur gagne, False sinon.
    """
    clear_console()
    print("\n")
    tries = 5
    code = [random.randint(0, 9) for _ in range(6)]

    print(Fore.CYAN + "Bienvenue dans le jeu Mastermind !")
    print("=" * 60)
    print(
        "Vous devez deviner un code à 6 chiffres.\n"
        "Vous avez 5 essais pour le trouver.\n"
        "À chaque essai, vous recevrez des indices sur votre réponse.\n"
        "Pourquoi pas appeler le numéro magique du helpdesk "
        "pour de l'aide ? ;)\n"
    )
    print(Fore.YELLOW + "=" * 60)

    while tries > 0:
        essai = input(
            "Essai #{} - Il vous reste {} essai(s). ".format(6 - tries, tries)
            + "Entrez un code à 6 chiffres : "
        ).strip()

        if essai == MAGIC_CODE:
            print(
                "Comment osez-vous appeler le helpdesk ! "
                "Vous avez gagné cette fois...."
            )
            return True

        if len(essai) != 6 or not essai.isdigit():
            print(Fore.RED + "Veuillez entrer un code valide à 6 chiffres.")
            continue

        guess = [int(digit) for digit in essai]

        if guess == code:
            print(Fore.GREEN + "Correct ! Vous avez deviné le bon nombre.")
            return True

        correct_position = sum(guess[i] == code[i] for i in range(6))
        correct_digits = (
            sum(min(guess.count(d), code.count(d)) for d in set(guess))
            - correct_position
        )

        print(
            Fore.RED
            + f"Faux ! {correct_position} chiffre(s) correct(s) à la bonne position, "
            + f"{correct_digits} chiffre(s) correct(s) mais à la mauvaise position."
        )
        print("\n")
        tries -= 1

    print(
        Fore.MAGENTA
        + f"Vous avez perdu ! Le code était {''.join(map(str, code))}."
    )
    return False
