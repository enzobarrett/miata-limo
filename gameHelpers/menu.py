import curses

from textHelpers.textline import TextLine


class Menu:
    def __init__(self, config, *options):
        self.config = config
        self.win = config.win

        self.menuItems = []
        maxLen = 0

        for menuOption in options:
            if len(menuOption) > maxLen:
                maxLen = len(menuOption)
            self.menuItems.append(TextLine(menuOption))

        self.currIndex = 0

        # highlight the first item
        self.menuItems[0].highlighted = True

        # define what the height and width should be
        self.width = maxLen + 4
        self.height = len(self.menuItems) * 2 + 2

    def incIndex(self):
        if self.currIndex == len(self.menuItems) - 1:
            self.currIndex = 0;
        else:
            self.currIndex += 1;

    def decIndex(self):
        if self.currIndex == 0:
            self.currIndex = len(self.menuItems) - 1;
        else:
            self.currIndex -= 1;

    def next(self):
        # un-highlight current menu item, highlight next one
        self.menuItems[self.currIndex].highlighted = False
        # increment index, looping back if at end of array
        self.incIndex()
        # highlight new menu item
        self.menuItems[self.currIndex].highlighted = True

    def prev(self):
        # un-highlight current menu item, highlight previous one
        self.menuItems[self.currIndex].highlighted = False
        # decrement index, looping back if at beginning of array
        self.decIndex()
        # highlight new menu item
        self.menuItems[self.currIndex].highlighted = True

    # display menu with current option highlighted
    def render(self):
        menuNum = 0
        y = self.config.halfHeight - self.height/2
        x = self.config.halfWidth - self.width/2

        y = int(y)
        x = int(x)

        for i in range(self.height):
            self.win.move(y, x)

            if i == 0:
                # top line
                self.win.addstr("+" + (self.width-2) * "-" + "+")
            elif i % 2 == 0:
                # even lines are menu items
                self.win.addstr("|")

                # use the REVERSE attr if the menuItem obj has highlight enabled
                if self.menuItems[menuNum].highlighted:
                    self.win.addstr('{:^{}s}'.format(self.menuItems[menuNum].txt, self.width-2), curses.A_REVERSE)
                else:
                    self.win.addstr('{:^{}s}'.format(self.menuItems[menuNum].txt, self.width-2))
                self.win.addstr("|")
                menuNum += 1
            else:
                # blank lines are blank-ish
                self.win.addstr("|" + " " * (self.width-2) + "|")

            y += 1

        # print bottom line
        self.win.move(y, x)
        self.win.addstr("+" + (self.width - 2) * "-" + "+")

        self.win.refresh()



