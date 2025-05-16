from utils.normalize import normalize
from .game2_check_letters import check_letters
from utils.colorama import Fore, Style

def play_game(secret_word, original_word): # Main game loop where the player attempts to guess the secret word.
    attempts = 6  # Attempts counter
    total_attempts = 0
    has_won = False

    while attempts > 0:  # Attempt counter and word check loop
        word = normalize(input("\nEntrez un mot de 5 lettres : ").strip())  # Normalize user input
        if len(word) == 5:  # Validate user input word length
            result = check_letters(word, secret_word)  # Compare the word with the secret word
            print("\n" + Fore.MAGENTA + "="*60 + Style.RESET_ALL)
            print(f"🔍 Résultat de l'essai : {Fore.CYAN}{result}{Style.RESET_ALL}")
            print(f"💡 Mot entré : {Fore.YELLOW}{word}{Style.RESET_ALL}")
            print(f"🔄 Essais restants : {Fore.GREEN}{attempts}{Style.RESET_ALL}")
            print(Fore.MAGENTA + "="*60 + Style.RESET_ALL + "\n")
            if word == secret_word:  # If the word is correct, end the game
                print(f"{Fore.GREEN}{Style.BRIGHT}🎉 Félicitations ! Vous avez deviné le mot secret '{secret_word}' en {total_attempts + 1} essais ! 🎉{Style.RESET_ALL}")
                has_won = True
                break
            attempts -= 1
            total_attempts += 1
        else:
            print(f"\n{Fore.RED}❌ Mot invalide. Veuillez entrer un mot de 5 lettres.{Style.RESET_ALL}")
    
    if not has_won:  # If the user has exhausted all attempts, reveal the secret word
        print("\n" + Fore.MAGENTA + "="*60 + Style.RESET_ALL)
        print(f"{Fore.RED}Dommage ! Vous avez perdu. Le mot secret était : '{original_word}'.{Style.RESET_ALL}")
        print(Fore.MAGENTA + "="*60 + Style.RESET_ALL)
    return has_won
