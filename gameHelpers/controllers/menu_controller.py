import curses


class MenuController:
    def __init__(self, menu):
        self.menu = menu

    def handle_input(self, c):
        if c == curses.KEY_DOWN or c == curses.KEY_RIGHT:
            self.menu.next()
        elif c == curses.KEY_UP or c == curses.KEY_LEFT:
            self.menu.prev()

    def render(self):
        self.menu.render()