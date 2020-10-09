import unittest

from cursesHelpers.winConfig import WinConfig
from gameHelpers.gameElements.limo import Limo


class TestLimo(unittest.TestCase):
    def setUp(self):
        self.config = WinConfig()
        self.testLimo = Limo(self.config, (16, 12), '1')

    # test config window init
    def test_config(self):
        self.assertEqual(self.testLimo.win, None)

    # test x init
    def test_x(self):
        self.assertEqual(self.testLimo.x, 12)

    # test y init
    def test_y(self):
        self.assertEqual(self.testLimo.y, 16)

    # test char init
    def test_ch(self):
        self.assertEqual(self.testLimo.char, '1')


if __name__ == '__main__':
    unittest.main()
