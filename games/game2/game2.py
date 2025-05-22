from .game2_introduction import introduction
from .game2_initialise_game import initialize_game
from .game2_play_game import play_game

def play():         # Main game function and boot to game manager
    introduction()
    secret_word, original_word = initialize_game()
    return play_game(secret_word, original_word, difficulty="")