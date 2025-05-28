import sys
import os

def wait_for_any_key():
    if os.name == 'nt': # For Windows
        input()
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