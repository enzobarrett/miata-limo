import unittest
from gameHelpers.router import Router
from gameHelpers.menu import Menu
from cursesHelpers.winConfig import WinConfig


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.router = Router(WinConfig())

    def test_menu_init(self):
        self.assertIsInstance(self.router.initialMenu, Menu)


if __name__ == '__main__':
    unittest.main()
