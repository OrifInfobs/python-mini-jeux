def get_valid_input(prompt, valid_options):
    """
    Demande une entrée utilisateur jusqu'à ce qu'elle soit dans les options valides.

    Args:
        prompt (str): Le message à afficher à l'utilisateur.
        valid_options (list): Liste des options valides (en minuscules).

    Returns:
        str: L'option choisie, toujours en minuscules.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Entrée invalide. Veuillez choisir parmi : {', '.join(valid_options)}.")
            
def get_integer_input(prompt, min_value=None, max_value=None):
    """
    Demande à l'utilisateur un entier valide, éventuellement dans une plage spécifiée.

    Args:
        prompt (str): Le message à afficher.
        min_value (int, optional): Valeur minimale acceptée.
        max_value (int, optional): Valeur maximale acceptée.

    Returns:
        int: L'entier saisi par l'utilisateur.
    """
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit():
            value = int(user_input)
            if (min_value is None or value >= min_value) and (max_value is None or value <= max_value):
                return value
            else:
                print(f"Veuillez entrer un nombre entre {min_value} et {max_value}.")
        else:
            print("Veuillez entrer un nombre entier valide.")