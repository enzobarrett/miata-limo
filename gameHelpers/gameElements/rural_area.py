import random


class RuralArea:
    def __init__(self, urbanArea):
        self.config = urbanArea.config

        # find if we are going to be lower or upper
        if urbanArea.yPos < self.config.halfHeight:
            self.pos = 'down'
        else:
            self.pos = 'up'

        # set starting y
        if self.pos == 'down':
            self.yPos = urbanArea.yPos + urbanArea.height
        else:
            self.yPos = 2

        # inherit starting x from urbanArea
        self.xPos = urbanArea.xPos

        # find if we are left or right
        if self.xPos < self.config.halfWidth:
            self.hPos = 'left'
        else:
            self.hPos = 'right'

        self.width = urbanArea.width
        self.height = self.config.height - 4 - urbanArea.height + 1

        # init road starting points with two different random values
        self.startPos1 = random.choice(urbanArea.intersections)
        self.startPos2 = random.choice(urbanArea.intersections)

        while self.startPos1 == self.startPos2:
            self.startPos1 = random.choice(urbanArea.intersections)
            self.startPos2 = random.choice(urbanArea.intersections)

        self.seed = random.randrange(1000000)

    def render(self):
        # determine what road has space to curve
        if self.hPos == 'left':
            if self.startPos1 < self.startPos2:
                straightRoad = self.startPos2
                curvyRoad = self.startPos1
            else:
                straightRoad = self.startPos1
                curvyRoad = self.startPos2
        else:
            if self.startPos1 > self.startPos2:
                straightRoad = self.startPos1
                curvyRoad = self.startPos2
            else:
                straightRoad = self.startPos2
                curvyRoad = self.startPos1

        self.draw_straight_road(straightRoad)

        self.draw_curvy_road(curvyRoad)

        self.config.win.refresh()

    def draw_straight_road(self, straightRoad):
        # draw the straight roads
        if self.pos == 'up':
            for y in range(self.height):
                self.config.win.move(self.yPos + self.height - 2 - y, straightRoad - 1)
                self.config.win.addstr("|")
        else:
            for y in range(self.height):
                self.config.win.move(self.yPos + y, self.xPos + self.width - straightRoad)
                self.config.win.addstr("|")

    def draw_curvy_road(self, curvyRoad):
        # draw the curvy road with a random curve
        # we use random with a preset seed in __init__ so the road won't change on render
        rand = random.Random()
        rand.seed(self.seed)

        xOffset = 0

        if self.pos == 'up':
            for y in range(self.height):
                self.config.win.move(self.yPos + self.height - 2 - y, curvyRoad - 1 + xOffset)
                self.config.win.addstr("\\")

                if y % rand.randint(1, 3) == 0:
                    if self.hPos == 'left':
                        xOffset -= 1
                    else:
                        xOffset += 1
        else:
            for y in range(self.height):
                self.config.win.move(self.yPos + y, self.xPos + self.width - curvyRoad + xOffset)
                self.config.win.addstr("\\")

                if y % rand.randint(1, 4) == 0:
                    if self.hPos == 'left':
                        xOffset -= 1
                    else:
                        xOffset += 1
