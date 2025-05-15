from .initialise_game import initialize_game
from .play_game import play_game

def check_word(): # Main function to start the game
    print("============================================================")
    original_word, secret_word = initialize_game()
    return play_game(secret_word, original_word)


