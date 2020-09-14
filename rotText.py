import time


class RotText:
    def __init__(self, filename, windowHeight, windowWidth, objectH, objectW):
        self.xOffset = 0
        self.sleepTime = .03

        self.wHeight = windowHeight
        self.wWidth = windowWidth
        self.objH = objectH
        self.objW = objectW - 1

        # read file and put each line into self.text
        file = open(filename, 'r')
        self.text = file.readlines()

    def display(self, window):
        offset = None
        lineNum = 0

        window.clear()

        if self.wWidth - self.objW - self.xOffset < 0:
            offset = -(self.wWidth - self.objW - self.xOffset)

        # loop through each line of text
        for line in self.text:
            # Start with the first line of text

            # running off screen logic
            if offset is not None:
                window.move(int(self.wHeight / 2) - int(self.objH / 2 + 1) + lineNum, 0)
            else:
                window.move(int(self.wHeight / 2) - int(self.objH / 2 + 1) + lineNum,
                            self.wWidth - self.objW - self.xOffset)

            window.addstr(line[offset:])

            lineNum += 1

        window.refresh()
        self.xOffset += 1

    def move(self, window):
        for x in range(0, self.wWidth):
            self.display(window)
            time.sleep(self.sleepTime)
            if self.sleepTime > .01:
                self.sleepTime -= .001
