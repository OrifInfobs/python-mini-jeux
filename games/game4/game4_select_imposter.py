import random
from games.game4.game4_liste_intrus import intrus, infosAnnexes
from utils.normalize import normalize

def select_theme_and_imposter(): # Function to randomly select a theme and an imposter word
    available_themes = random.sample(list(intrus.keys()), 5) # Select 5 random themes from the available keys in the `intrus` dictionary
    print("Choisissez un thème parmi les options suivantes :")
    for i, theme in enumerate(available_themes, start=1):
        info = infosAnnexes.get(theme, "Aucune information disponible") # Safely get the info or a default message
        print(f"{i}. {theme} ({info})") # Display the themes with their corresponding numbers
    while True:
        try: # Check for valid input as player chooses a theme
            choice = int(input("\nEntrez le numéro correspondant à votre choix : ").strip()) # Get the player's choice
            if 1 <= choice <= len(available_themes):
                selected_theme = available_themes[choice - 1]
                break
            else:
                print("Veuillez entrer un numéro valide entre 1 et 5.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro.")
    normal_words, imposter_words = intrus[selected_theme] # Retrieve the normal and imposter words for the selected theme
    normal_words = [normalize(word) for word in normal_words] # Normalize all words
    imposter_word = normalize(imposter_words[0])
    return selected_theme, normal_words, imposter_word