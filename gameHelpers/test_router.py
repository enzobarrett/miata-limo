import unittest
from gameHelpers.router import Router
from gameHelpers.menu import Menu
from cursesHelpers.winConfig import WinConfig


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.router = Router(WinConfig())

    def test_state_increment(self):
        self.assertEqual(self.router.state, 0)

        # a new line should increment the state
        self.router.route("\n")
        self.assertEqual(self.router.state, 1)

        # a new line should increment the state
        self.router.route("\n")
        self.assertEqual(self.router.state, 2)

    def test_menu_init(self):
        self.assertIsInstance(self.router.initialMenu, Menu)


if __name__ == '__main__':
    unittest.main()
