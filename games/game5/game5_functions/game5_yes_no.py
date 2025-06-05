"""
Ask the user a yes/no question and return their response as a boolean.
"""


def ask_yes_no(prompt):
    """
    Prompt the user with a yes/no question and return True for yes,
    False for no.

    Args:
        prompt (str): The question to ask the user.

    Returns:
        bool: True if the user answers yes, False otherwise.
    """
    while True:
        response = input(f"{prompt} (o/n) : ").strip().lower()
        if response in ("o", "oui", "y", "yes"):
            return True
        if response in ("n", "non", "no"):
            return False
        print("Veuillez répondre par 'o' (oui) ou 'n' (non).")
