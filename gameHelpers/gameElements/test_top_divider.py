import unittest

from cursesHelpers.winConfig import WinConfig
from gameHelpers.gameElements.top_divider import TopDivider


class TestTopDivider(unittest.TestCase):
    def setUp(self):
        self.config = WinConfig()
        self.config.width = 100
        self.config.height = 26
        self.divider = TopDivider(self.config)

    # config correctly initialized
    def test_config(self):
        self.assertIsInstance(self.divider.config, WinConfig)

    # width correctly initialized
    def test_width(self):
        self.assertEqual(self.divider.width, self.config.width)

    # half width correctly initialized
    def test_half_width(self):
        self.assertEqual(self.divider.halfWidth, self.config.halfWidth)


if __name__ == '__main__':
    unittest.main()
