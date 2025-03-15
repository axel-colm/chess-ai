from typing import Tuple
import chess
from chessai.evaluation import evaluate_material, evaluate_mobility

def evaluate(board: chess.Board, maximizing_player: chess.Color):
    """
    Evaluate the board.
    
    Args:
        board (chess.Board): The board to evaluate.
        maximizing_player (chess.Color): The player to maximize.
        
    Returns:
        int: The evaluation score.
    """
    return evaluate_material(board, maximizing_player) + evaluate_mobility(board, maximizing_player)

    
def minimax(board: chess.Board, depth: int, maximizing_player: chess.Color) -> Tuple[int, chess.Move]:
    """
    Perform minimax search on the board.
    
    Args:
        board (chess.Board): The board to search.
        depth (int): The depth to search.
        maximizing_player (chess.Color): The player to maximize.
        
    Returns:
        int: The evaluation score.
        Move: The best move.
    """
    if depth == 0 or board.is_game_over():
        return evaluate(board, maximizing_player), None
    
    best_move = None
    best_score = -float('inf') if board.turn == maximizing_player else float('inf')
    
    for move in board.legal_moves:
        # Make the move
        board.push(move)
        score, _ = minimax(board, depth - 1, maximizing_player)
        board.pop()
        
        # Maximizing the score 
        if board.turn == maximizing_player:
            if score > best_score:
                best_score = score
                best_move = move
        # Minimizing the score
        else:
            if score < best_score:
                best_score = score
                best_move = move
                
    return best_score, best_move

