import sys
sys.path.append('..')
import unittest
import chess
from chessai.minimax import minimax, evaluate

class TestMinimax(unittest.TestCase):
    def test_minimax(self):
        board = chess.Board()
        while not board.is_game_over():
            w_score = evaluate(board, chess.WHITE)
            b_score = evaluate(board, chess.BLACK)
            print(board.unicode(empty_square="."))
            print(f"White: {w_score}")
            print(f"Black: {b_score}")
            print("___\n")
            
            score, move = minimax(board, 3, board.turn)
            board.push(move)
        self.assertTrue(board.is_game_over())
         
            
        
if __name__ == '__main__':
    unittest.main()
