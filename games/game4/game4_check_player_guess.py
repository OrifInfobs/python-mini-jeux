"""
Check the player's guess against the imposter word for Game 4.
"""


def check_player_guess(imposter_word, shuffled_words):
    """
    Check the player's guess against the imposter word.
    Args:
        imposter_word (str): The imposter word to find.
        shuffled_words (list[str]): The list of shuffled words.
    Returns:
        bool: True if the player found the imposter, False otherwise.
    """
    while True:
        try:
            prompt = "\nEntrez le numéro correspondant à votre choix : "
            choice = int(input(prompt).strip())
            if 1 <= choice <= len(shuffled_words):
                selected_word = shuffled_words[choice - 1]
                break
            else:
                print("Veuillez entrer un numéro valide entre 1 et 4.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro.")
    if selected_word == imposter_word:
        print("\nFélicitations ! Vous avez trouvé l'intrus 🎉")
        return True
    else:
        print("\nDésolé, ce n'est pas le bon mot.")
        print(f"L'intrus était : {imposter_word}")
        return False
