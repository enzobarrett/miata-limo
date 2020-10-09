import unittest

from cursesHelpers.winConfig import WinConfig
from gameHelpers.controllers.limo_controller import LimoController
from gameHelpers.scanners.perimeter_entrance_scanner import PerimeterEntranceScanner


class TestLimoController(unittest.TestCase):
    def setUp(self):
        self.config = WinConfig()
        self.scanner = PerimeterEntranceScanner(self.config)
        self.scanner.entrances = [(1, 2), (3, 4), (5, 6)]
        self.controller = LimoController(self.config, self.scanner)

    # test config init
    def test_config(self):
        self.assertIsInstance(self.controller.config, WinConfig)

    # test limo array init, should be empty
    def test_limo_array(self):
        self.assertEqual(self.controller.limos, [])

    # test instance scanner init
    def test_scanner(self):
        self.assertIsInstance(self.controller.scanner, PerimeterEntranceScanner)

    # tick should append a limo 1/80 times
    def test_tick(self):
        for x in range(1000):
            self.controller.tick()

        self.assertGreater(len(self.controller.limos), 0)


if __name__ == '__main__':
    unittest.main()
