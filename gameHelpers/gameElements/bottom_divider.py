import os
import getpass


class BottomDivider:
    def __init__(self, config):
        self.config = config
        self.yPos = config.height - 1
        self.width = self.config.width - 1

    def render(self):
        self.config.win.move(self.yPos, 0)

        usersName = getpass.getuser().upper() + " "
        paddedUsername = ' ' + '{:=<20}'.format(usersName)

        # we cannot write to the bottom right corner due to a curses quirk
        # spacing char
        c = "="
        self.config.win.addstr(c * 5 + paddedUsername + c * (self.width - 26))

        self.config.win.refresh()
