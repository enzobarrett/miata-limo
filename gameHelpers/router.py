import curses

from gameHelpers.controllers.menu_controller import MenuController
from gameHelpers.menu import Menu


class Router:
    def __init__(self, config):
        # 0 is single player, 1 is multi-player
        self.gameMode = None
        self.state = 0
        self.initialMenu = Menu(config, "Single Player", "Multiplayer")
        self.menuController = MenuController(self.initialMenu)

    def route(self, c):
        if c == curses.KEY_ENTER or c == 10 or c == 13:
            # before changing to gameplay, store gamemode from menu
            if self.state == 0:
                self.gameMode = self.menuController.menu.currIndex
            self.state += 1

        # if true, we are in the gamemode selection menu
        if self.state == 0:
            self.menuController.handle_input(c)
            self.menuController.render()

        # we are in gameplay
        # TODO: execute a method here
        if self.state == 1:
            pass
