import random
from .game4_liste_intrus import intrus, infosAnnexes
from utils.normalize import normalize
from utils.colorama import Fore, Style


def select_theme_and_imposter():
    choix = "\nChoisissez un thème parmi les options suivantes :\n"
    underlined_text_choix = "\x1B[4m" + choix + "\x1B[0m"
    available_themes = random.sample(list(intrus.keys()), 5)
    print(underlined_text_choix)
    for i, theme in enumerate(available_themes, start=1):
        info = infosAnnexes.get(theme)
        print(f"\n{i}. {Fore.YELLOW}{theme}{Style.RESET_ALL} ({info})")
    while True:
        try:
            prompt = "\n Entrez le numéro correspondant à votre choix :"
            choice = int(input(prompt).strip())  # Get the player's choice
            if 1 <= choice <= len(available_themes):
                selected_theme = available_themes[choice - 1]
                break
            else:
                print("Veuillez entrer un numéro valide entre 1 et 5.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro.")
    normal_words, imposter_words = intrus[selected_theme]
    normal_words = [normalize(word) for word in normal_words]
    imposter_word = normalize(imposter_words[0])
    return selected_theme, normal_words, imposter_word
