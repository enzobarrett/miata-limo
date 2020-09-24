from textHelpers.textline import TextLine


class Menu:
    def __init__(self, config, *options):
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
        self.width = maxLen + 2
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

