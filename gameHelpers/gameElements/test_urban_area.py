import unittest

from cursesHelpers.winConfig import WinConfig
from gameHelpers.gameElements.urban_area import UrbanArea


class TestUrbanArea(unittest.TestCase):
    def setUp(self):
        self.config = WinConfig()
        self.config.width = 100
        self.urban = UrbanArea(self.config, 15, 10)

    # width should be config width / 2 - 1
    def test_width(self):
        self.assertEqual(self.urban.width, 49)

    # x and y should be accurate to what was passed in
    def test_x(self):
        self.assertEqual(self.urban.xPos, 10)

    def test_y(self):
        self.assertEqual(self.urban.yPos, 15)


if __name__ == '__main__':
    unittest.main()
