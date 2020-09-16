import time


class RotText:
    def __init__(self, config, filename, objectW, objectH):
        self.xOffset = 0
        self.sleepTime = .03

        self.wHeight = config.height
        self.wWidth = config.width
        self.objH = objectH
        self.objW = objectW
        self.win = config.win

        # read file and put each line into self.text
        file = open(filename, 'r')
        self.text = file.readlines()

    def display(self):
        offset = None
        lineNum = 0

        self.win.clear()

        if self.wWidth - self.objW - self.xOffset < 0:
            offset = -(self.wWidth - self.objW - self.xOffset)

        # loop through each line of text
        for line in self.text:
            # run off screen logic
            if offset is not None:
                self.win.move(int(self.wHeight / 2) - int(self.objH / 2 + 1) + lineNum, 0)
            else:
                self.win.move(int(self.wHeight / 2) - int(self.objH / 2 + 1) + lineNum,
                              self.wWidth - self.objW - self.xOffset)

            self.win.addstr(line[offset:])

            lineNum += 1

        self.win.refresh()
        self.xOffset += 1

    def move(self):
        for x in range(0, self.wWidth):
            self.display()
            time.sleep(self.sleepTime)
            if self.sleepTime > .01:
                self.sleepTime -= .001
