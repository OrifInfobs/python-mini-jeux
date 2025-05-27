def check_player_guess(imposter_word, shuffled_words):      # Function to check the player's guess against the imposter word
    while True:
        try:
            choice = int(input("\nEntrez le numéro correspondant à votre choix : ").strip())      # Get player's choice as a number + error handling
            if 1 <= choice <= len(shuffled_words):
                selected_word = shuffled_words[choice - 1]
                break
            else:
                print("Veuillez entrer un numéro valide entre 1 et 4.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro.")
    if selected_word == imposter_word:         # Check if the selected word is the imposter word and give win if yes
        print("\nFélicitations ! Vous avez trouvé l'intrus 🎉")
        return True
    else:                                      # If the selected word is not the imposter word, reveal the imposter word and give loss
        print(f"\nDésolé, ce n'est pas le bon mot. L'intrus était : {imposter_word}")
        return False
