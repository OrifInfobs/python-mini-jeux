import os
from utils.press_any_key import wait_for_any_key

def introduction() :
    Clear = lambda : os.system ("cls")
    Clear()
    print("===========================================================================================================================================================================================================================================================")
    print("Bienvenue dans le 5e mini jeu. Il s'agit d'un sudoku. Il vous faut donc remplire les cases vides avec des nombres de 1 à 9. Vous devez cependant faire attention à ne pas placer le même nombre dans la même colone, la même ligne ou le même carré de 3x3.") 
    print("===========================================================================================================================================================================================================================================================")
    
    wait_for_any_key()
introduction()