class Limo:
    # TODO: add velocity
    # TODO: update constructor to take tuple cords
    def __init__(self, config, cords, ch):
        self.win = config.win
        self.x = cords[1]
        self.y = cords[0]
        self.char = ch

    def render(self):
        self.win.move(self.y, self.x)
        self.win.addstr('L' + self.char)
        self.win.refresh()