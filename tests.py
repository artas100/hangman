import unittest
from unittest.mock import patch
from game import Game  # Assuming your class is in a file called game.py


class TestGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_select_word_easy(self, mock_input):
        game = Game()
        word = game.select_word(1)
        self.assertIn(word, game.words["easy"])

    @patch('builtins.input', side_effect=['2'])
    def test_select_word_medium(self, mock_input):
        game = Game()
        word = game.select_word(2)
        self.assertIn(word, game.words["medium"])

    @patch('builtins.input', side_effect=['3'])
    def test_select_word_hard(self, mock_input):
        game = Game()
        word = game.select_word(3)
        self.assertIn(word, game.words["hard"])


if __name__ == '__main__':
    unittest.main()
