from time import sleep
import os
from typing import Any

board: list[Any] = list(range(1, 10))

#J'ai copy paste ce code trouvé sur Github x)

def check_board(plyr):
    winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
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
        move_p = int(input((f"Your turn({num}) choose your move: (1-9) ---> ",)))
        if move_p not in range(1, 10):
            continue
        if board[move_p - 1] == move_p:
            board[move_p - 1] = shape
            break
    print_board()
    if check_board(shape):
        print((f"Player({num}) WINS",))
        return "tictactoe_win"

def computer_move():
    moves = ((0, 2, 6, 8), (4,), (1, 3, 5, 7))

    for i in range(0, 9):
        if board[i] == i + 1:
            board[i] = "O"
            if check_board("O"):
                print_board()
                print("Computer WINS")
                return "lose" 
            else:
                board[i] = i + 1
    h = 0
    for k in range(0, 9):
        if board[k] == k + 1:
            board[k] = "X"
            if check_board("X"):
                board[k] = "O"
                h = 1
                break
            else:
                board[k] = k + 1

    if h == 0:
        ch = 0
        for tup in moves:
            for i in tup:
                if board[i] == i + 1:
                    board[i] = 'O'
                    ch = 1
                    break
            if ch == 1:
                break

    print_board()
    return None  

def print_board():
    os.system('cls')
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n\n"
        if i == 'X':
            print((f"[{i}]", "red"), end=end)
        elif i == 'O':
            print((f"[{i}]", "blue"), end=end)
        else:
            print(f"[{i}]", end=end)
        j += 1

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
        x = input("......... \n"
                  "1.What?\n"
                  "2.Wtf\n"
                  "3.Escape!\n"
                  " What is going on?")
        if x in ['1', '2', '3']:
            os.system('cls')
            print('3 seconds until start...')
            sleep(3)
            result = start_AI()
            return result  
        else:
            os.system('cls')
            print('pls enter a number')
def TicTacToe():
    return menu()