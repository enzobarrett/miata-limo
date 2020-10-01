import curses
import sys
import time
import signal

from cursesHelpers.winConfig import WinConfig
from gameHelpers.menu import Menu
from textHelpers.rotText import RotText
from textHelpers.text import Text
from gameHelpers.router import Router


class Game:
    def __init__(self):
        # setup control-c handling to terminate program
        signal.signal(signal.SIGINT, self.signal_handler)

        # init curses
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)

        # make getch() non blocking
        self.stdscr.nodelay(1)

        # store window details
        self.config = WinConfig()

        # set window in config class
        self.config.win = self.stdscr

    # main game loop
    def run(self):
        # check that the terminal is the correct size
        self.size_or_terminate()

        # init router now that we have config vars
        self.router = Router(self.config)

        # display the splash screens
        self.splash_screen()
        time.sleep(1.5)
        self.splash_screen2()
        time.sleep(1)

        c = None

        # run the game loop
        while True:
            # start by clearing the screen
            self.stdscr.clear()

            # TODO: tick time that takes into consideration render time

            # get char, pass to router
            c = self.stdscr.getch()
            self.router.route(c)

            # TODO: replace with non-hardcoded tick time
            time.sleep(.125)

    ### splash screens ###

    def splash_screen(self):
        splash = Text(self.config, 40, 12)
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
        rotText = RotText(self.config, "limo.txt", 49, 8)
        rotText.move()

    ### curses helpers ###

    # refresh default window
    def refresh(self):
        self.stdscr.refresh()

    ### termination functions ###

    def size_or_terminate(self):
        y, x = self.stdscr.getmaxyx()

        # set some helper vars
        self.config.height = y
        self.config.width = x
        self.config.halfHeight = int(y / 2)
        self.config.halfWidth = int(x / 2)

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
