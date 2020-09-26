import curses

from gameHelpers.menu import Menu

class Router:
    def __init__(self, config):
        self.state = 0
        self.initialMenu = Menu(config, "Single Player", "Multiplayer")

    def route(self, c):
        if c == curses.KEY_ENTER or c == 10 or c == 13:
            self.state += 1
