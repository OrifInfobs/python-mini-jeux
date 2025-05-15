import os
from games.game4.game_function import game_start
def Clear():
    os.system("cls")
def play(): # Main function when game is called
    while True:
        Clear()
        print("""
============================================================
🎉 BIENVENUE DANS LE MINI JEUX TROUVEZ L'INTRUS 🎉
============================================================

L'objectif est de trouver le mot intrus parmi les 4 qui seront listés. Vous devez trouver le mot secret en choisissant
parmi les 4 mots proposés.

Bonne chance! 
              
============================================================
        """)
        return game_start()