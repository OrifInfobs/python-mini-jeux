from .introduction import introduction
from .initialise_game import initialize_game
from .play_game import play_game

def play(): # Main game function and boot to game manager
    introduction()
    print("============================================================")
    original_word, secret_word = initialize_game()
    return play_game(secret_word, original_word)
