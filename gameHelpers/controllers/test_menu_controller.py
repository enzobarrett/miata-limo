import curses
import unittest

from cursesHelpers.winConfig import WinConfig
from gameHelpers.menu import Menu
from gameHelpers.controllers.menu_controller import MenuController


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.config = WinConfig()
        self.controller = MenuController(Menu(self.config, "test1", "test2", "test3"))

    # pressing right arrow or down array should increment menu
    def test_next_key(self):
        self.controller.handle_input(curses.KEY_RIGHT)
        self.assertEqual(self.controller.menu.currIndex, 1)

        self.controller = MenuController(Menu(self.config, "test1", "test2", "test3"))
        self.controller.handle_input(curses.KEY_DOWN)
        self.assertEqual(self.controller.menu.currIndex, 1)

    # pressing left arrow or up array should decrement menu
    def test_next_key(self):
        self.controller.handle_input(curses.KEY_LEFT)
        self.assertEqual(self.controller.menu.currIndex, 2)

        self.controller = MenuController(Menu(self.config, "test1", "test2", "test3"))
        self.controller.handle_input(curses.KEY_UP)
        self.assertEqual(self.controller.menu.currIndex, 2)

if __name__ == '__main__':
    unittest.main()
