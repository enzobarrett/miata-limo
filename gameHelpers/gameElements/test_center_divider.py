import unittest

from cursesHelpers.winConfig import WinConfig
from gameHelpers.gameElements.center_divider import CenterDivider


class TestUrbanArea(unittest.TestCase):
    def setUp(self):
        self.config = WinConfig()
        self.config.width = 100
        self.config.height = 26
        self.divider = CenterDivider(self.config)

    # should have correct starting x
    def test_xPos(self):
        self.assertEqual(self.divider.xPos, 49)

    # height should be the same as config
    def test_height(self):
        self.assertEqual(self.divider.height, self.config.height)

if __name__ == '__main__':
    unittest.main()
