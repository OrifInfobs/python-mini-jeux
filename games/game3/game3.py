import random
import os
import sys
from colorama import init, Fore, Style
init(autoreset=True)

Clear = lambda : os.system ("cls")
# Logique de cette fonction à remplacer par le jeux choisi
def play():
    Clear()
    print(Fore.CYAN + "Bienvenue dans ce mini-jeux qui mêle hasard et mémoire !  ")
    print("L’objectif : Vous devez tirer autant de carte nécessaire pour atteindre un score de 100 points. Chaque carte correspond à un nombre de point entre 1 et 10.  ")
    print("Vous commencez avec 0 points, et chaque carte s’additionne à votre score. Retenez bien votre score, car lorsque vous tirez une nouvelle carte, la précédente sera masqué. ")
    print("Après chaque tirage, vous avez deux choix : (1) Continuer et tirer une nouvelle carte, (2) terminer la partie. Lorsque vous terminez la partie, vous devrez alors indiquer de combien de points vous avez dépassé 100. Si vous donnez la bonne différence, vous remportez la partie, dans le cas contraire, vous perdez.  ")
    print("Si vous décidez de continuer à tirer des cartes, mais que vous avez déjà dépassez 100, vous perdez également la partie et le jeu s’arrête.  ")
    def wait_for_any_key():
        if os.name == 'nt': # For Windows
            import msvcrt
            print(Fore.MAGENTA + "Bonne chance ! Appuyez sur n’importe quelle touche pour lancer le jeu. ")
            msvcrt.getch()
        else: # For Unix-like systems
            import termios
            import tty
            print(Fore.MAGENTA + "Bonne chance ! Appuyez sur n’importe quelle touche pour lancer le jeu. ")
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    wait_for_any_key()
    Clear()
    boucle = 1
    total = 0
    while boucle > 0 :
        pioche = random.randint(1, 10)
        print(Fore.BLUE + "Choisir l’une de ces deux actions : ")
        print(Fore.YELLOW + "1. Continuer et tirer une nouvelle carte. ")
        print(Fore.YELLOW + "2. Arrêter la partie ")
        try:
            prochaineAction = int(input(Fore.CYAN + "Quel est votre prochaine action ? (Entrez 1 ou 2) : "))
        except ValueError:
            print(Fore.RED + "Entrée invalide. Veuillez entrer 1 ou 2.")
            continue

        Clear()
        if prochaineAction == 1 and total >= 100 :
            boucle = 0
            print(Fore.RED + "C’est perdu ! Vous avez demandé à tirer une nouvelle carte. Le but du jeu est de s’arrêter dès que vous dépassez 100 points, et vous êtes à " + str(total + pioche) + " points.")
            return False
        elif prochaineAction == 1 :
            print(Fore.GREEN + "Nouvelle carte piochée ! Vous avez obtenu " + str(pioche) + " points.  ")
            total = total + pioche
        if prochaineAction == 2 and total < 100 :
            boucle = 0
            print(Fore.RED + "C’est perdu ! Vous avez arrêté la partie, mais vous avez un score de " + str(total) + " points. Il faut au minimum obtenir un score de 100 avant d’arrêter la partie")
            return False
        elif prochaineAction == 2 : 
            boucle = 0
            calculation = int(input(Fore.CYAN + "Bien joué, vous venez de dépasser 100 points. Pour gagner la partie, veuillez rentrer de combien de points vous avez dépassé 100 :  "))
            if calculation == (total - 100) :
                print(Fore.GREEN + "C’est gagné ! Vous avez bien arrêté dès que vous avez dépassé les 100 points, et vous avez pu donner la bonne différence. Vous avez dépassé 100 de " + str(total-100) + " points.")
                return True
            else :
                print(Fore.RED + "C’est perdu ! Vous avez bien arrêté dès que vous avez dépassé les 100 points, mais vous n’avez pas donner la bonne différence. Vous avez dépassé 100 de " + str(total-100) + " points. ")
                return False