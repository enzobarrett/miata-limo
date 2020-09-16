class Text:
    def __init__(self, config, w, h):
        self.x = config.halfWidth - int(w / 2)
        self.y = config.halfHeight - int(h / 2)
        self.win = config.win
        self.yCounter = 0

    # prints the given string to the screen and moves the cursor down one line
    def addstr(self, string):
        self.win.move(self.y + self.yCounter, self.x)
        self.win.addstr(string)
        self.yCounter += 1
