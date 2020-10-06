import unittest

from cursesHelpers.winConfig import WinConfig
from gameHelpers.scanners.perimeter_entrance_scanner import PerimeterEntranceScanner


class TestPerimeterEntranceScanner(unittest.TestCase):
    def setUp(self):
        self.config = WinConfig()
        self.scanner = PerimeterEntranceScanner(self.config)

    # config should be properly initialized
    def test_config(self):
        self.assertIsInstance(self.scanner.config, WinConfig)

    # entrances array should initially be blank
    def test_entrances(self):
        self.assertEqual(self.scanner.entrances, [])

    # array of entrance chars should be initialized
    def test_entrance_chars(self):
        self.assertEqual(self.scanner.entranceChars, ['\\', '-', '|'])


if __name__ == '__main__':
    unittest.main()
