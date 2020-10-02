import unittest

from cursesHelpers.winConfig import WinConfig
from gameHelpers.controllers.game_controller import GameController
from gameHelpers.gameElements.urban_area import UrbanArea


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.config = WinConfig()
        self.controller = GameController(self.config)

    def test_initial_urban_area(self):
        self.assertIsInstance(self.controller.urbanAreas, list)


if __name__ == '__main__':
    unittest.main()
