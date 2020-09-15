class Text:
    def __init__(self, y, x, win):
        self.x = x
        self.y = y
        self.win = win
        self.yCounter = 0

    # prints the given string to the screen and moves the cursor down one line
    def addstr(self, string):
        self.win.move(self.y + self.yCounter, self.x)
        self.win.addstr(string)
        self.yCounter += 1