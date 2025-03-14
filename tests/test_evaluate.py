import chess
import pytest
from chessai.evaluation import (
    evaluate_material
)

def log_board_and_scores(board, wscore, bscore, eval_func_name):
    print(board.unicode(empty_square="."))
    print(f"{eval_func_name} - White score: {wscore}")
    print(f"{eval_func_name} - Black score: {bscore}")
    print("---")


def test_evaluate_material():
    # Position initiale
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    wscore = evaluate_material(board, chess.WHITE)
    bscore = evaluate_material(board, chess.BLACK)
    try:
        assert wscore == 0, f"Expected 0, got {wscore}"
        assert bscore == 0, f"Expected 0, got {bscore}"
    except AssertionError as e:
        log_board_and_scores(board, wscore, bscore, "Material")
        raise e

    # Noirs avec un avantage matériel
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1")
    wscore = evaluate_material(board, chess.WHITE)
    bscore = evaluate_material(board, chess.BLACK)
    try:
        assert wscore < 0, f"Expected positive score, got {wscore}"
        assert bscore > 0, f"Expected negative score, got {bscore}"
    except AssertionError as e:
        log_board_and_scores(board, wscore, bscore, "Material")
        raise e

    # Blancs avec un avantage matériel
    board = chess.Board("rnbqkbnr/pppp1ppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    wscore = evaluate_material(board, chess.WHITE)
    bscore = evaluate_material(board, chess.BLACK)
    try:
        assert wscore > 0, f"Expected negative score, got {wscore}"
        assert bscore < 0, f"Expected positive score, got {bscore}"
    except AssertionError as e:
        log_board_and_scores(board, wscore, bscore, "Material")
        raise e

    # Qween value (9)
    board = chess.Board("7k/7q/8/8/8/8/8/7K w - - 0 1")
    wscore = evaluate_material(board, chess.WHITE)
    bscore = evaluate_material(board, chess.BLACK)
    try:
        assert wscore == -9, f"Expected 9, got {wscore}"
        assert bscore == 9, f"Expected -9, got {bscore}"
    except AssertionError as e:
        log_board_and_scores(board, wscore, bscore, "Material")
        raise e

    # Rook value (5)
    board = chess.Board("7k/7r/8/8/8/8/8/7K w - - 0 1")
    wscore = evaluate_material(board, chess.WHITE)
    bscore = evaluate_material(board, chess.BLACK)
    try:
        assert wscore == -5, f"Expected 5, got {wscore}"
        assert bscore == 5, f"Expected -5, got {bscore}"
    except AssertionError as e:
        log_board_and_scores(board, wscore, bscore, "Material")
        raise e

    # 2 Bishop value (3 + 3)
    # -> 1 Bishop is insufficient to checkmate (score = 0)
    board = chess.Board("7k/7b/7b/8/8/8/8/7K w - - 0 1")
    wscore = evaluate_material(board, chess.WHITE)
    bscore = evaluate_material(board, chess.BLACK)
    try:
        assert wscore == -6, f"Expected 6, got {wscore}"
        assert bscore == 6, f"Expected -6, got {bscore}"
    except AssertionError as e:
        log_board_and_scores(board, wscore, bscore, "Material")
        raise e

    # 2 Knight value (3 + 3)
    # -> 1 Knight is insufficient to checkmate (score = 0)
    board = chess.Board("7k/7n/7n/8/8/8/8/7K w - - 0 1")
    wscore = evaluate_material(board, chess.WHITE)
    bscore = evaluate_material(board, chess.BLACK)
    try:
        assert wscore == -6, f"Expected 6, got {wscore}"
        assert bscore == 6, f"Expected -6, got {bscore}"
    except AssertionError as e:
        log_board_and_scores(board, wscore, bscore, "Material")
        raise e

    # Pawn value (1)
    board = chess.Board("7k/7p/8/8/8/8/8/7K w - - 0 1")
    wscore = evaluate_material(board, chess.WHITE)
    bscore = evaluate_material(board, chess.BLACK)
    try:
        assert wscore == -1, f"Expected 1, got {wscore}"
        assert bscore == 1, f"Expected -1, got {bscore}"
    except AssertionError as e:
        log_board_and_scores(board, wscore, bscore, "Material")
        raise e

    # Stalemate
    board = chess.Board("8/8/8/8/8/6K1/7Q/7k w - - 0 1")
    board.turn = chess.BLACK
    wscore = evaluate_material(board, chess.WHITE)
    bscore = evaluate_material(board, chess.BLACK)
    try:
        assert wscore == 9999, f"Expected 9999, got {wscore}"
        assert bscore == -9999, f"Expected -9999, got {bscore}"
    except AssertionError as e:
        log_board_and_scores(board, wscore, bscore, "Material")
        raise e

    # Insufficient material
    board = chess.Board("8/8/8/8/8/6B1/5K2/7k w - - 0 1")
    wscore = evaluate_material(board, chess.WHITE)
    bscore = evaluate_material(board, chess.BLACK)
    try:
        assert wscore == 0, f"Expected 0, got {wscore}"
        assert bscore == 0, f"Expected 0, got {bscore}"
    except AssertionError as e:
        log_board_and_scores(board, wscore, bscore, "Material")
        raise e

    # Pat
    board = chess.Board("8/8/8/8/8/7k/5q2/7K w - - 0 1")
    board.turn = chess.WHITE
    wscore = evaluate_material(board, chess.WHITE)
    bscore = evaluate_material(board, chess.BLACK)
    try:
        assert wscore == 0, f"Expected 0, got {wscore}"
        assert bscore == 0, f"Expected 0, got {bscore}"
    except AssertionError as e:
        log_board_and_scores(board, wscore, bscore, "Material")
        raise e
