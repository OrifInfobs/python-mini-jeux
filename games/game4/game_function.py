from games.game4.check_player_guess import check_player_guess
from games.game4.select_imposter import select_theme_and_imposter
from games.game4.shuffle import shuffle_list

def game_start(): # Main internal game function
    while True:
        theme, normal_words, imposter_word = select_theme_and_imposter() # Select theme and imposter word
        words_with_imposter = normal_words + [imposter_word] # Combine and shuffle words
        shuffled_words = shuffle_list(words_with_imposter) # Display shuffled words
        if check_player_guess(imposter_word, shuffled_words): # Check player's guess
            return True
        else:
            return False