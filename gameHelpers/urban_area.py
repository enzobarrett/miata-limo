class UrbanArea:
    def __init__(self, config):
        self.config = config

        # width of area should be half - 1 for a separation line
        self.width = int((self.config.width / 2) - 1)

    # draws a simple city grid
    # TODO: give options for different types of city grids
    def render(self):
        for x in range(7):
            # TODO: make x a argument for the constructor
            self.config.win.move(17+x, 0)

            # if we are on a even line, it is a street
            if x % 2 == 0:
                self.config.win.addstr(33 * '-' + "+---+---+---+---")
            elif x % 2 == 1:
                self.config.win.addstr(('`' * 33) + "|```|```|```|```")
        self.config.win.refresh()
