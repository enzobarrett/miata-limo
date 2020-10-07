class Limo:
    # TODO: add velocity
    def __init__(self, config, y, x, ch):
        self.win = config.win
        self.x = x
        self.y = y
        self.char = ch

    def render(self):
        self.win.move(self.y, self.x)
        self.win.addstr('L' + self.char)
        self.win.refresh()