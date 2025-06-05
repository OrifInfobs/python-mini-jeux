"""
TicTacToe mini-game for the random words game (Mots Aléatoires).
"""
from time import sleep
import os
import random
from typing import Any
from colorama import Fore, Style
from utils.press_any_key import wait_for_any_key

board: list[Any] = list(range(1, 10))


def tictactoe():
    """
    Launch the TicTacToe mini-game and return the result.
    Returns:
        str: 'win', 'lose', or 'draw'.
    """
    global board
    board = list(range(1, 10))
    return menu()


def check_board(plyr):
    """
    Check if the given player has won the game.
    Args:
        plyr (str): Player symbol ('X' or 'O').
    Returns:
        str or None: 'tictactoe_win' if win, None otherwise.
    """
    winners = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )
    for tup in winners:
        if all(board[j] == plyr for j in tup):
            return "tictactoe_win"
    return None


def player_move(num, shape):
    """
    Handle the player's move.
    Args:
        num (int): Player number.
        shape (str): Player symbol ('X').
    Returns:
        str or None: 'tictactoe_win' if win, None otherwise.
    """
    while True:
        try:
            move_p = int(input(f"Your turn({num}): "))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 9.")
            continue
        if move_p not in range(1, 10):
            print(
                "Choix hors limites. Veuillez entrer un nombre entre 1 et 9."
            )
            continue
        if board[move_p - 1] == move_p:
            board[move_p - 1] = shape
            break
        else:
            print("Cette case est déjà prise. Choisissez-en une autre.")
    print_board()
    if check_board(shape):
        print(f"Player({num}) WINS")
        return "tictactoe_win"
    return None


def computer_move():
    """
    Handle the computer's move.
    Returns:
        str or None: 'lose' if computer wins, None otherwise.
    """
    for i in range(9):
        if board[i] == i + 1:
            board[i] = "O"
            if check_board("O"):
                print_board()
                print("Computer WINS")
                return "lose"
            board[i] = i + 1
    for i in range(9):
        if board[i] == i + 1:
            board[i] = "X"
            if check_board("X"):
                board[i] = "O"
                print_board()
                return None
            board[i] = i + 1
    available = [i for i in range(9) if board[i] == i + 1]
    if available:
        move = random.choice(available)
        board[move] = "O"
    print_board()
    return None


def print_board():
    """
    Print the current TicTacToe board.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n   1   2   3")
    print("  -------------")
    for row in range(3):
        row_str = f"{row+1} |"
        for col in range(3):
            val = board[row * 3 + col]
            if val == 'X':
                cell = f"{Fore.RED}X{Style.RESET_ALL}"
            elif val == 'O':
                cell = f"{Fore.BLUE}O{Style.RESET_ALL}"
            else:
                cell = f"{val}"
            row_str += f" {cell} |"
        print(row_str)
        print("  -------------")


def start_ai():
    """
    Start the AI vs player TicTacToe game loop.
    Returns:
        str: 'win', 'lose', or 'draw'.
    """
    print_board()
    turn = 1
    while turn != 10:
        if turn % 2 != 0:
            result = player_move(1, 'X')
            if result == "tictactoe_win":
                return "win"
        if turn % 2 == 0:
            print("Computer be thinkin'... ")
            sleep(2)
            result = computer_move()
            if result == "lose":
                return "lose"
        turn += 1
    return "draw"


def menu():
    """
    Display the TicTacToe menu and start the game.
    Returns:
        str: 'win', 'lose', or 'draw'.
    """
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            "......... \n"
            "\n1. What?\n"
            "\n2. Wtf is this\n"
            "\n3. Escape!\n"
        )
        wait_for_any_key()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('3 seconds until start...')
        sleep(3)
        result = start_ai()
        return result
