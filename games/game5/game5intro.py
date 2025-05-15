def introduction() :
    import os
    import sys
    Clear = lambda : os.system ("cls")
    Clear()
    print("===========================================================================================================================================================================================================================================================")
    print("Bienvenue dans le 5e mini jeu. Il s'agit d'un sudoku. Il vous faut donc remplire les cases vides avec des nombres de 1 à 9. Vous devez cependant faire attention à ne pas placer le même nombre dans la même colone, la même ligne ou le même carré de 3x3.") 
    print("===========================================================================================================================================================================================================================================================")
    def wait_for_any_key():
        if os.name == 'nt': # For Windows
            import msvcrt
            print("Pour commencer la partie, appuyez sur n'importe quelle touche. ")
            msvcrt.getch()
        else: # For Unix-like systems
            import termios
            import tty
            print("Pour commencer la partie, appuyez sur n'importe quelle touche. ")
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    wait_for_any_key()
introduction()