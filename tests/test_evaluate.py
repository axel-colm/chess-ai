import sys
sys.path.append("..")
import chess
import unittest
from chessai.evaluation import (
    evaluate_material
)

def log_board_and_scores(board, wscore, bscore, eval_func_name):
    print(board.unicode(empty_square="."))
    print(f"{eval_func_name} - White score: {wscore}")
    print(f"{eval_func_name} - Black score: {bscore}")
    print("---")

class TestEvaluateMaterial(unittest.TestCase):
    
    def test_initial_board(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")    
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertEqual(wscore, 0)
        self.assertEqual(bscore, 0)
    
    def test_black_advantage(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1")
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertLess(wscore, 0)
        self.assertGreater(bscore, 0)
        
    def test_white_advantage(self):
        board = chess.Board("rnbqkbnr/pppp1ppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertGreater(wscore, 0)
        self.assertLess(bscore, 0)
        
    def test_queen_value(self):
        board = chess.Board("7k/7q/8/8/8/8/8/7K w - - 0 1")
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertEqual(wscore, -9)
        self.assertEqual(bscore, 9)
        
    def test_rook_value(self):
        board = chess.Board("7k/7r/8/8/8/8/8/7K w - - 0 1")
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertEqual(wscore, -5)
        self.assertEqual(bscore, 5)
        
    def test_bishop_value(self):
        # 1 Bishop is insufficient to checkmate (score = 0)
        # 2 Bishop value (3 + 3)
        board = chess.Board("7k/7b/7b/8/8/8/8/7K w - - 0 1")
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertEqual(wscore, -6)
        self.assertEqual(bscore, 6)
        
    def test_knight_value(self):
        # 1 Knight is insufficient to checkmate (score = 0)
        # 2 Knight value (3 + 3)
        board = chess.Board("7k/7n/7n/8/8/8/8/7K w - - 0 1")
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertEqual(wscore, -6)
        self.assertEqual(bscore, 6)
        
    def test_pawn_value(self):
        board = chess.Board("7k/7p/8/8/8/8/8/7K w - - 0 1")
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertEqual(wscore, -1)
        self.assertEqual(bscore, 1)
        
    def test_stalemate(self):
        board = chess.Board("8/8/8/8/8/6K1/7Q/7k w - - 0 1")
        board.turn = chess.BLACK
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertEqual(wscore, 9999)
        self.assertEqual(bscore, -9999)
        
    def test_insufficient_material(self):
        board = chess.Board("8/8/8/8/8/6B1/5K2/7k w - - 0 1")
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertEqual(wscore, 0)
        self.assertEqual(bscore, 0)
        
    def test_pat(self):
        board = chess.Board("8/8/8/8/8/7k/5q2/7K w - - 0 1")
        board.turn = chess.WHITE
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertEqual(wscore, 0)
        self.assertEqual(bscore, 0)        

if __name__ == "__main__":
    unittest.main()