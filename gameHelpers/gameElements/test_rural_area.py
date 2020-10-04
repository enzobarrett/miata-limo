import unittest

from cursesHelpers.winConfig import WinConfig
from gameHelpers.gameElements.rural_area import RuralArea
from gameHelpers.gameElements.urban_area import UrbanArea


class TestRuralArea(unittest.TestCase):
    def setUp(self):
        self.config = WinConfig()
        self.config.width = 100
        self.config.halfWidth = 50
        self.config.height = 26
        self.config.halfHeight = 13

        self.urban1 = UrbanArea(self.config, 17, 0)
        self.urban2 = UrbanArea(self.config, 2, 51)

    # area should correctly determine if it is up or down
    def test_position(self):
        self.rural = RuralArea(self.urban1)
        self.assertEqual(self.rural.pos, 'up')

        self.rural = RuralArea(self.urban2)
        self.assertEqual(self.rural.pos, 'down')

    # area should correctly determine if it is left or right
    def test_hPosition(self):
        self.rural = RuralArea(self.urban1)
        self.assertEqual(self.rural.hPos, 'left')

        self.rural = RuralArea(self.urban2)
        self.assertEqual(self.rural.hPos, 'right')

    # correct start y
    def test_yPos(self):
        self.rural = RuralArea(self.urban1)
        self.assertEqual(self.rural.yPos, 2)

        self.rural = RuralArea(self.urban2)
        self.assertEqual(self.rural.yPos, 9)

    # correct start x
    def test_xPos(self):
        self.rural = RuralArea(self.urban1)
        self.assertEqual(self.rural.xPos, 0)

        self.rural = RuralArea(self.urban2)
        self.assertEqual(self.rural.xPos, 51)

    # correct height calculated based off rural area height
    def test_height(self):
        self.rural = RuralArea(self.urban1)
        self.assertEqual(self.rural.height, 16)

        self.rural = RuralArea(self.urban2)
        self.assertEqual(self.rural.height, 16)

    # width should be the same as the urban area
    def test_width(self):
        self.rural = RuralArea(self.urban1)
        self.assertEqual(self.rural.width, self.urban1.width)

        self.rural = RuralArea(self.urban2)
        self.assertEqual(self.rural.width, self.urban2.width)

    # the RuralArea should select 2 different intersections from the UrbanArea
    def test_random_intersection_selection(self):
        self.rural = RuralArea(self.urban1)
        self.assertIsInstance(self.rural.startPos1, int)
        self.assertIsInstance(self.rural.startPos2, int)
        self.assertNotEqual(self.rural.startPos1, self.rural.startPos2)

        self.rural = RuralArea(self.urban2)
        self.assertIsInstance(self.rural.startPos1, int)
        self.assertIsInstance(self.rural.startPos2, int)
        self.assertNotEqual(self.rural.startPos1, self.rural.startPos2)


if __name__ == '__main__':
    unittest.main()
