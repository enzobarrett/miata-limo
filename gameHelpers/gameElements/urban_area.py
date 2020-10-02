class UrbanArea:
    def __init__(self, config, y, x):
        self.config = config

        # width of area should be half - 1 for a separation line
        self.width = int((self.config.width / 2) - 1)

        # starting position of city grid
        self.yPos = y
        self.xPos = x

    # draws a simple city grid
    # TODO: give options for different types of city grids
    def render(self):
        for yOffset in range(7):
            self.config.win.move(self.yPos+yOffset, self.xPos)

            # if we are on a even line, it is a street
            if yOffset % 2 == 0:
                self.config.win.addstr(33 * '-' + "+---+---+---+---")
            elif yOffset % 2 == 1:
                self.config.win.addstr((' ' * 33) + "|   |   |   |   ")
        self.config.win.refresh()
