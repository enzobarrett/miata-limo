import time

# draws a top divider with the current unix timestamp
class TopDivider:
    def __init__(self, config):
        self.config = config
        self.width = config.width
        self.halfWidth = config.halfWidth

    def render(self):
        self.config.win.move(0, 0)

        # construct timestamp string
        timestamp = '  ' + str(int(time.time())) + '  '

        widthOffset = self.halfWidth - 7
        paddingStr = '=' * widthOffset

        toAdd = paddingStr + timestamp + paddingStr
        self.config.win.addstr(toAdd)

        self.config.win.refresh()
