import unittest

from cursesHelpers.winConfig import WinConfig
from gameHelpers.gameElements.bottom_divider import BottomDivider


class TestUrbanArea(unittest.TestCase):
    def setUp(self):
        self.config = WinConfig()
        self.config.width = 100
        self.config.height = 26
        self.divider = BottomDivider(self.config)

    # should have correct config instance variable
    def test_config(self):
        self.assertIsInstance(self.divider.config, WinConfig)

    # should have a starting y position at the bottom of the screen
    def test_yPos(self):
        self.assertEqual(self.divider.yPos, self.config.height - 1)

    # width should be one less than config
    # avoids curses quirk with drawing in bottom right corner
    def test_width(self):
        self.assertEqual(self.divider.width, self.config.width - 1)


if __name__ == '__main__':
    unittest.main()
