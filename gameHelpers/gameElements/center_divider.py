class CenterDivider:
    def __init__(self, config):
        self.config = config

        self.xPos = int((self.config.width / 2) - 1)
        self.height = self.config.height

    def render(self):
        for y in range(self.height):
            self.config.win.move(y, self.xPos)
            self.config.win.addstr("||")

        self.config.win.refresh()
