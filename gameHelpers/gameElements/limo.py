class Limo:
    # TODO: add velocity
    # TODO: update constructor to take tuple cords
    def __init__(self, config, cords, ch):
        self.win = config.win
        self.x = cords[1]
        self.y = cords[0]
        self.char = ch

        # set velocity based on spawn position
        self.xVel = 0
        self.yVel = 0

        if self.y == 24:
            self.yVel = -1
        if self.y == 1:
            self.yVel = 1
        if self.x == 98:
            self.xVel = -1
        if self.x == 0:
            self.xVel = 1

    def render(self):
        self.win.move(self.y, self.x)
        self.win.addstr('L' + self.char)
        self.win.refresh()