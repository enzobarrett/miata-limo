import unittest
from gameHelpers.menu import Menu
from cursesHelpers.winConfig import WinConfig


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.config = WinConfig()
        self.config.win = False

    # Window should be correctly set in menu
    def test_window(self):
        self.menu = Menu(self.config, "Item1")
        self.assertFalse(self.menu.win)

    # TextLine obj of first menu item should be highlighted
    def test_first_item_highlight(self):
        self.menu = Menu(self.config, "Item1")
        self.assertTrue(self.menu.menuItems[0].highlighted)

    # width should be largest menu item + 2
    def test_width(self):
        self.menu = Menu(self.config, "12345", "123456", "1234567")
        self.assertEqual(self.menu.width, 7 + 4)

        self.menu = Menu(self.config, "123456", "123456789", "12")
        self.assertEqual(self.menu.width, 9 + 4)

    # height should be number of menu items * 2 + 2
    def test_height(self):
        self.menu = Menu(self.config, "12345", "123456", "1234567")
        self.assertEqual(self.menu.height, 6 + 2)

        self.menu = Menu(self.config, "123456", "123456789", "12", "123456")
        self.assertEqual(self.menu.height, 8 + 2)

    # when next() is called, the next item should be highlighted
    def test_next(self):
        self.menu = Menu(self.config, "12345", "123456", "1234567")
        self.assertTrue(self.menu.menuItems[0].highlighted)
        self.assertFalse(self.menu.menuItems[1].highlighted)

        self.menu.next()
        self.assertFalse(self.menu.menuItems[0].highlighted)
        self.assertTrue(self.menu.menuItems[1].highlighted)

        self.menu.next()
        self.assertFalse(self.menu.menuItems[1].highlighted)
        self.assertTrue(self.menu.menuItems[2].highlighted)

        # testing rollover
        self.menu.next()
        self.assertFalse(self.menu.menuItems[2].highlighted)
        self.assertTrue(self.menu.menuItems[0].highlighted)

    # when prev() is called, the previous item should be highlighted
    def test_prev(self):
        self.menu = Menu(self.config, "12345", "123456", "1234567")
        self.assertTrue(self.menu.menuItems[0].highlighted)
        self.assertFalse(self.menu.menuItems[2].highlighted)

        self.menu.prev()
        self.assertFalse(self.menu.menuItems[0].highlighted)
        self.assertTrue(self.menu.menuItems[2].highlighted)

        self.menu.prev()
        self.assertFalse(self.menu.menuItems[2].highlighted)
        self.assertTrue(self.menu.menuItems[1].highlighted)

        # testing rollover
        self.menu.prev()
        self.assertFalse(self.menu.menuItems[1].highlighted)
        self.assertTrue(self.menu.menuItems[0].highlighted)


if __name__ == '__main__':
    unittest.main()
