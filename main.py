import curses
import sys
import time
import signal

from rotText import RotText
from text import Text


class Game:
    def __init__(self):
        # setup control-c handling to terminate program
        signal.signal(signal.SIGINT, self.signal_handler)

        # init curses
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)

    # main game loop
    def run(self):
        # check that the terminal is the correct size
        self.size_or_terminate()

        # display the splash screens
        self.splash_screen()
        time.sleep(1)
        self.splash_screen2()
        time.sleep(1)

        c = None

        # run the game loop
        while True:
            c = self.stdscr.getch()
            self.stdscr.addch(c)

    ### splash screens ###

    def splash_screen(self):
        splash = Text(self.halfheight - 7, self.halfwidth - 20, self.stdscr)
        splash.addstr(r" __  __ _       _                       ")
        splash.addstr(r"|  \/  (_)     | |                      ")
        splash.addstr(r"| \  / |_  __ _| |_ __ _                ")
        splash.addstr(r"| |\/| | |/ _` | __/ _` |               ")
        splash.addstr(r"| |  | | | (_| | || (_| |               ")
        splash.addstr(r"|_|  |_|_|\__,_|\__\__,_|               ")
        splash.addstr(r"               _      _                 ")
        splash.addstr(r"              | |    (_)                ")
        splash.addstr(r"              | |     _ _ __ ___   ___  ")
        splash.addstr(r"              | |    | | '_ ` _ \ / _ \ ")
        splash.addstr(r"              | |____| | | | | | | (_) |")
        splash.addstr(r"              |______|_|_| |_| |_|\___/ ")
        self.refresh()

    def splash_screen2(self):
        rotText = RotText("limo.txt", 26, 100, 8, 49)
        rotText.move(self.stdscr)

    ### curses helpers ###

    # refresh default window
    def refresh(self):
        self.stdscr.refresh()

    ### termination functions ###

    def size_or_terminate(self):
        y, x = self.stdscr.getmaxyx()

        # set some helper vars
        self.height = y
        self.width = x
        self.halfheight = int(y / 2)
        self.halfwidth = int(x / 2)

        # if screen is not the correct size, terminate
        if not (y == 26 and x == 100):
            self.terminate()
            print("Screen is wrong size (%dx%d): please resize to 100x26" % (x, y))
            self.exit()

    # gracefully handles control-c and terminates
    def signal_handler(self, sig, frame):
        self.terminate()
        self.exit()

    def terminate(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    # shortcut for sys.exit
    def exit(self):
        sys.exit()


def main():
    game = Game()
    game.run()
    game.terminate()


if __name__ == "__main__":
    main()
