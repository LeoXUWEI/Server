import unittest
import logic

class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        # Test the get_winner
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

        board = [
            ['X', None, 'O'],
            [None, 'O', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), None)

        board = [
            ['X', None, 'O'],
            [None, 'O', None],
            ['O', 'X', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')

        # Test the other_player
        player = 'X'
        self.assertEqual(logic.other_player(player), 'O')

        player = 'O'
        self.assertEqual(logic.other_player(player), 'X')

        # Test the board_update
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        row = 1
        col = 1
        self.assertEqual(logic.board_update(board, row, col, 'X'), False)

        row = 2
        col = 3
        self.assertEqual(logic.board_update(board, row, col, 'X'), True)

        row = 2
        col = 3
        self.assertEqual(logic.board_update(board, row, col, 'X'), False)

    # TODO: Test all functions from logic.py!

if __name__ == '__main__':
    unittest.main()
