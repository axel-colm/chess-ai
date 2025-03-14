import sys
sys.path.append("..")
import chess
import unittest
from chessai.evaluation import (
    evaluate_material,
    evaluate_mobility
)

def log_board_and_scores(board, wscore, bscore, eval_func_name):
    print("---")
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
        
    def test_checkmate_white_wins(self):
        """
        Test the material evaluation when white checkmates black.
        """
        board = chess.Board("8/8/8/8/8/K7/1Q6/k7 b - - 0 1")
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertEqual(wscore, 9999, "White should have a score of 9999 when checkmating black")
        self.assertEqual(bscore, -9999, "Black should have a score of -9999 when checkmated by white")

    def test_checkmate_black_wins(self):
        """
        Test the material evaluation when black checkmates white.
        """
        board = chess.Board("K7/1q6/k7/8/8/8/8/8 w - - 0 1")
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertEqual(wscore, -9999, "White should have a score of -9999 when checkmated by black")
        self.assertEqual(bscore, 9999, "Black should have a score of 9999 when checkmating white")

    def test_stalemate(self):
        """
        Test the material evaluation when the game is a stalemate.
        """
        board = chess.Board("K7/8/1q6/k7/8/8/8/8 w - - 0 1")
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertEqual(wscore, 0, "Material score should be 0 in a stalemate")
        self.assertEqual(bscore, 0, "Material score should be 0 in a stalemate")
        
    def test_insufficient_material(self):
        board = chess.Board("8/8/8/8/8/6B1/5K2/7k w - - 0 1")
        wscore = evaluate_material(board, chess.WHITE)
        bscore = evaluate_material(board, chess.BLACK)
        self.assertEqual(wscore, 0)
        self.assertEqual(bscore, 0)
        

class TestEvaluateMobility(unittest.TestCase):
    
    def test_initial_board(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")    
        wscore = evaluate_mobility(board, chess.WHITE)
        bscore = evaluate_mobility(board, chess.BLACK)
        self.assertEqual(wscore, 0)
        self.assertEqual(bscore, 0)
    
    def test_white_advantage(self):
        """
        Test the mobility evaluation when white has a mobility advantage.
        """
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        board.push_san("e4")
        wscore = evaluate_mobility(board, chess.WHITE)
        bscore = evaluate_mobility(board, chess.BLACK)
        self.assertGreater(wscore, 0, "White should have a positive mobility score")
        self.assertLess(bscore, 0, "Black should have a negative mobility score")

    def test_black_advantage(self):
        """
        Test the mobility evaluation when black has a mobility advantage.
        """
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 1")
        board.push_san("e5")
        wscore = evaluate_mobility(board, chess.WHITE)
        bscore = evaluate_mobility(board, chess.BLACK)
        self.assertLess(wscore, 0, "White should have a negative mobility score")
        self.assertGreater(bscore, 0, "Black should have a positive mobility score")
        
if __name__ == "__main__":
    unittest.main()