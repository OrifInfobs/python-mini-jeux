from time import sleep
import os
from typing import Any
from colorama import Fore, Style
import random
from utils.press_any_key import wait_for_any_key

board: list[Any] = list(range(1, 10))

# J'ai copy paste ce code que j'ai trouvé sur Github x)

def TicTacToe():
    global board
    board = list(range(1, 10))  # Had to define this since otherwise it would load previous state
    return menu()

def check_board(plyr):
    winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8),             # All winning combinations
               (0, 3, 6), (1, 4, 7), (2, 5, 8),
               (0, 4, 8), (2, 4, 6))
    for tup in winners:
        win = True
        for j in tup:
            if board[j] != plyr:
                win = False
                break
        if win:
            return "tictactoe_win"
    return None

def plyer_move(num, shape):
    while True:
        try:
            move_p = int(input(f"Your turn({num}): "))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 9.")
            continue
        if move_p not in range(1, 10):
            print("Choix hors limites. Veuillez entrer un nombre entre 1 et 9.")
            continue
        if board[move_p - 1] == move_p:
            board[move_p - 1] = shape
            break
        else:
            print("Cette case est déjà prise. Choisissez-en une autre.")

    print_board()
    if check_board(shape):
        print((f"Player({num}) WINS",))
        return "tictactoe_win"

def computer_move():
    for i in range(0, 9):
        if board[i] == i + 1:
            board[i] = "O"
            if check_board("O"):
                print_board()
                print("Computer WINS")
                return "lose"
            else:
                board[i] = i + 1

    for i in range(0, 9):
        if board[i] == i + 1:
            board[i] = "X"
            if check_board("X"):
                board[i] = "O"
                print_board()
                return None
            else:
                board[i] = i + 1

    available = [i for i in range(9) if board[i] == i + 1]
    if available:
        move = random.choice(available)         # Randomize moves so game is easier, but will try to win if under threat
        board[move] = "O"
    print_board()
    return None

def print_board():
    os.system('cls')
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

def start_AI():
    print_board()
    turn = 1
    while turn != 10:
        if turn % 2 != 0:
            result = plyer_move(1, 'X')
            if result == "tictactoe_win":
                return "win"
        if turn % 2 == 0:
            print("Computer be thinkin'... ")
            sleep(2)
            result = computer_move()
            if result == "lose":
                return "lose"
        turn += 1
    else:
        return "draw"

def menu():
    while True:
        Clear = lambda: os.system('cls')
        Clear()
        print("......... \n"
              "\n1. What?\n"
              "\n2. Wtf is this\n"
              "\n3. Escape!\n")
        wait_for_any_key()
        os.system('cls')
        print('3 seconds until start...')
        sleep(3)
        result = start_AI()
        return result