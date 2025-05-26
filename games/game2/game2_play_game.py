from utils.colorama import Fore, Style
from utils.normalize import normalize
from .game2_check_letters import check_letters
from utils.rainbow import rainbow_text
from .game2_TicTacToe import TicTacToe
import os

def play_game(secret_word, original_word, difficulty):
    attempts = 6
    total_attempts = 0
    has_won = False

    while attempts > 0:
        word = normalize(input("\nEntrez un mot de 5 lettres : ").strip())
        if len(word) == 5:
            result = check_letters(word, secret_word)
            print("\n" + Fore.MAGENTA + "="*60 + Style.RESET_ALL)
            print(f"🔍 Résultat de l'essai : {Fore.CYAN}{result}{Style.RESET_ALL}")
            print(f"💡 Mot entré : {Fore.YELLOW}{word}{Style.RESET_ALL}")
            print(f"🔄 Essais restants : {Fore.GREEN}{attempts}{Style.RESET_ALL}")
            print(Fore.MAGENTA + "="*60 + Style.RESET_ALL + "\n")
            if word == original_word and difficulty == "Difficile":
                print(rainbow_text(f"Félicitations ! Vous avez deviné le mot {original_word}' en {total_attempts + 1} essais en mode Difficile !"))
            if word == secret_word:
                print(f"{Fore.GREEN}{Style.BRIGHT}🎉 Félicitations ! Vous avez deviné le mot secret '{secret_word}' en {total_attempts + 1} essais ! 🎉{Style.RESET_ALL}")
                has_won = True
                break
            if word == "croix":
                print(Fore.CYAN + "Easter egg déclenché ! Lancement du TicTacToe...")
                ttt_result = TicTacToe()
                if ttt_result == "win":
                    return "tictactoe_win"
                elif ttt_result in ("lose", "draw"):
                    return False
            attempts -= 1
            total_attempts += 1
    if not has_won:
        print("\n" + Fore.MAGENTA + "="*60 + Style.RESET_ALL)
        print(f"{Fore.RED}Dommage ! Vous avez perdu. Le mot secret était : '{original_word}'.{Style.RESET_ALL}")
    return has_won