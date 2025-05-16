from game_manager import start_new_game, play_single_game
from utils.input_handler import get_valid_input
from utils.colorama import Fore, Style
def main_menu():
    while True:
        print(Fore.CYAN + Style.BRIGHT + "\n+ === Bienvenue dans les Mini-Jeux du Terminal ===")
        print("1. Nouvelle Partie")
        print(Fore.LIGHTYELLOW_EX + "2. Accès développeur (Choisir un mini-jeu)")
        print(Fore.MAGENTA + Style.DIM + "3. Sortir" + Style.RESET_ALL)
        choice = input("Votre choix (1, 2 ou 3) : ").strip()

        if choice == "1":
            start_new_game()
        elif choice == "2":
            choose_single_game()
        elif choice == "3":
            print("Merci d'avoir joué. À bientôt ! 👋")
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