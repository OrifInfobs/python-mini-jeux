import random
from colorama import Fore, Style
from utils.rainbow import rainbow_text
# Import des mini-jeux
from games.game4 import game4
from games.game1 import game1
from games.game2 import game2
from games.game3 import game3
from games.game5 import game5

def start_new_game():
    print("\nNouvelle partie commencée ! Bonne chance !\n")

    # Liste des mini-jeux à enchaîner
    games_list = [game1, game2, game3, game4, game5]
    random.shuffle(games_list)  # Optionnel : mélanger l'ordre des jeux

    for idx, game in enumerate(games_list, start=1):
        print(f"--- Mini-Jeu {idx} ---")
        result = game.play()

        if not result:
            print(Fore.RED + "\n💀 Vous avez perdu ! Fin de la partie.\n" + Style.RESET_ALL)
            return  # Fin de la partie si on perd un mini-jeu

        print("✅ Bravo, vous avez réussi ce mini-jeu !\n")

    print(rainbow_text("🎉 Félicitations, vous avez gagné tous les mini-jeux ! 🏆\n") + Style.RESET_ALL)

def play_single_game(game_number):
    """
    Permet de lancer un seul mini-jeu spécifique.
    """
    games_list = [game1, game2, game3, game4, game5]
    selected_game = games_list[game_number - 1]

    print(f"\n--- Lancement du Mini-Jeu {game_number} ---")
    result = selected_game.play()

    if result:
        print(Fore.LIGHTGREEN_EX + "✅ Vous avez réussi ce mini-jeu !\n" + Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX + "❌ Vous avez perdu ce mini-jeu.\n" + Style.RESET_ALL)
