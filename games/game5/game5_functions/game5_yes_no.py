def ask_yes_no(prompt):  # Function to ask the user a yes/no question
    while True:
        answer = input(prompt + " (Oui/Non) : ").strip().lower()
        if answer in ["oui", "o"]:
            return True
        elif answer in ["non", "n"]:
            return False
        else:
            print("Veuillez répondre par Oui ou Non.")