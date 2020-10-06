import curses
import time


# scans perimeter of game board to find all cords where a limo could be spawned
class PerimeterEntranceScanner:
    def __init__(self, config):
        self.config = config
        self.entrances = []
        self.entranceChars = ['\\', '-', '|']

    def scan(self):
        yBottom = 24
        yTop = 1
        xRight = 99
        xLeft = 1

        # scan horizontally
        for x in range(self.config.width):
            if not (x == 49 or x == 50):
                c1 = self.config.win.inch(yTop, x)
                c2 = self.config.win.inch(yBottom, x)

                if chr(c1) in self.entranceChars:
                    self.entrances.append((yTop, x))

                if chr(c2) in self.entranceChars:
                    self.entrances.append((yBottom, x))

        # scan vertically
        for y in range(1, self.config.height - 2):
            c1 = self.config.win.inch(y, xLeft)
            c2 = self.config.win.inch(y, xRight)

            if chr(c1) in self.entranceChars:
                self.entrances.append((y, xLeft))

            if chr(c2) in self.entranceChars:
                self.entrances.append((y, xRight))

