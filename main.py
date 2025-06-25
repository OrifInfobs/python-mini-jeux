from game_manager import start_new_game, play_single_game
from utils.input_handler import get_valid_input
from utils.colorama import Fore, Style
from utils.rainbow import rainbow_text
from time import sleep


def main_menu():
    while True:
        print(
            Fore.CYAN + Style.BRIGHT +
            "\n+ === Bienvenue aux mini-jeux python de Ryan! ===\n" +
            Style.RESET_ALL
        )
        print("\n1. Nouvelle Partie")
        print(
            Fore.LIGHTYELLOW_EX +
            "\n2. Accès développeur (Choisir un mini-jeu)"
        )
        print(Fore.BLACK + Style.DIM + "\n3. Sortir" + Style.RESET_ALL)
        choice = input("\nVotre choix (1, 2 ou 3) : ").strip()

        if choice == "1":
            start_new_game()
        elif choice == "2":
            choose_single_game()
        elif choice == "3":
            print(rainbow_text("Merci d'avoir joué. À bientôt ! 👋"))
            sleep(4)
            break
        else:
            print("Entrée invalide, veuillez choisir 1, 2 ou 3.")


def choose_single_game():
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "\n=== Choisissez un mini-jeu ===")
    print("1. Mini-Jeu 1")
    print("2. Mini-Jeu 2")
    print("3. Mini-Jeu 3")
    print("4. Mini-Jeu 4")
    print("5. Mini-Jeu 5")

    choice = get_valid_input("Votre choix (1-5) : ", ["1", "2", "3", "4", "5"])
    play_single_game(int(choice))


if __name__ == "__main__":
    main_menu()
