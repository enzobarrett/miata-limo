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

    ### Test Velocity

    # test pos x velocity
    def test_pos_x_vel(self):
        self.testLimo = Limo(self.config, (16, 0), '1')
        self.assertEqual(self.testLimo.xVel, 1)

    # test neg x velocity
    def test_neg_x_vel(self):
        self.testLimo = Limo(self.config, (16, 98), '1')
        self.assertEqual(self.testLimo.xVel, -1)

    # test pos y velocity
    def test_pos_y_vel(self):
        self.testLimo = Limo(self.config, (1, 14), '1')
        self.assertEqual(self.testLimo.yVel, 1)

    # test neg x velocity
    def test_neg_y_vel(self):
        self.testLimo = Limo(self.config, (24, 14), '1')
        self.assertEqual(self.testLimo.yVel, -1)


if __name__ == '__main__':
    unittest.main()
