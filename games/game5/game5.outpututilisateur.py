def userOutput() :
    from initGrid import is_valid
    startloop = 1
    modification = input("Permettre les modifications en cas d'erreur ? (Oui/Non)")
    while startloop == 1 :
        if modification == "Oui" :
            startloop = 0
        elif modification == "Non" :
            startloop = 0
        else :
            modification = input("Veuillez sélectionner (Oui) ou (Non) pour la modification d'erreur : ")
    # if the user wants to play without modifications allowed
    nextatempt = 10
    if modification == "Oui" :
        while nextatempt == 10 :
            row = int(input("Veuillez sélectionner la ligne de la case à remplir"))
            col = int(input("Veuillez maintenant sélectionner la colonne de la case à remplir"))
            num = int(input("Veuillez enfin sélectionner le nombre que vous voulez entrer (1-9)"))
            if is_valid != True :
                nextatempt = 0
    # if the user wants to play with modifications allowed
    else :
        while nextatempt >= 1 :
            row = int(input("Veuillez sélectionner la ligne de la case à remplir"))
            col = int(input("Veuillez maintenant sélectionner la colonne de la case à remplir"))
            num = int(input("Veuillez enfin sélectionner le nombre que vous voulez entrer (1-9)"))
            if is_valid != True :
                nextatempt = nextatempt - 1
                print("Vous devez modifier votre dernière réponse afin de continuer.")
            else : 
                    grid[row][col] = num

    
