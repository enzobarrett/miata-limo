import unittest
from textHelpers.textline import TextLine

class TestTextLine(unittest.TestCase):

    def test_initial_highlight(self):
        self.text = TextLine("test")
        self.assertFalse(self.text.highlighted)

    def test_initial_text(self):
        self.text = TextLine("test")
        self.assertEqual(self.text.txt, "test")


if __name__ == '__main__':
    unittest.main()
