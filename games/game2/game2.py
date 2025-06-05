"""
Main entry point for the random words game (Mots Aléatoires).
"""

from .game2_initialise_game import initialize_game
from .game2_check_letters import check_letters
from .game2_introduction import introduction
from .game2_TicTacToe import tictactoe
from utils.colorama import Fore, Style
from utils.rainbow import rainbow_text


def play():
    """
    Main function to play the random words game and easter egg TicTacToe.

    Args:
        None
    Returns:
        None or str: Returns 'tictactoe_win' if the TicTacToe easter egg is
        won, False if lost, otherwise None.
    """
    introduction()
    original_word, secret_word = initialize_game()
    attempts = 6
    has_won = False

    for attempt in range(1, attempts + 1):
        guess = input(
            f"{Fore.LIGHTYELLOW_EX}Essai {attempt}/{attempts} - "
            f"Entrez votre mot : {Style.RESET_ALL}"
        ).strip().lower()

        # Easter egg: launch TicTacToe if user types 'tictactoe'
        if guess == "tictactoe":
            print(
                Fore.CYAN +
                "Easter egg déclenché ! Lancement du TicTacToe..." +
                Style.RESET_ALL
            )
            ttt_result = tictactoe()
            if ttt_result == "win":
                print(
                    Fore.GREEN +
                    "Bravo ! Vous avez gagné au TicTacToe !" +
                    Style.RESET_ALL
                )
                print(
                    rainbow_text(
                        f"Félicitations ! Vous avez deviné le mot "
                        f"{original_word} en {attempt} essais en mode "
                        f"TicTacToe !"
                    )
                )
                print(
                    f"{Fore.GREEN}{Style.BRIGHT}🎉 Félicitations ! "
                    f"Vous avez deviné le mot secret '{secret_word}' "
                    f"en {attempt} essais ! 🎉{Style.RESET_ALL}"
                )
                return "tictactoe_win"
            elif ttt_result in ("lose", "draw"):
                print(
                    Fore.RED +
                    "Dommage ! Vous n'avez pas gagné au TicTacToe." +
                    Style.RESET_ALL
                )
                return False
            continue

        if guess == secret_word:
            print(
                f"{Fore.GREEN}{Style.BRIGHT}🎉 Félicitations ! "
                f"Vous avez deviné le mot secret '{secret_word}' "
                f"en {attempt} essais ! 🎉{Style.RESET_ALL}"
            )
            has_won = True
            break
        else:
            feedback = check_letters(guess, secret_word)
            print(f"{Fore.CYAN}Résultat : {feedback}{Style.RESET_ALL}")

    if not has_won:
        print(
            Fore.RED +
            f"Dommage ! Vous avez perdu. Le mot secret était : "
            f"'{original_word}'." +
            Style.RESET_ALL
        )
