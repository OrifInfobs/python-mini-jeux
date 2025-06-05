import sys
# Ignore errors it doesn't do anything
# Found this code on StackOverflow so I'm not sure how it works, but what matters is that it works

def wait_for_any_key():
    try:                        # Windows
        import msvcrt
        msvcrt.getch()
    except ImportError:         # Unix/Linux/Mac
        import termios
        import tty
        if not sys.stdin.isatty():
            input()
            return
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)   
        try:
            tty.setcbreak(fd)                   
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)    