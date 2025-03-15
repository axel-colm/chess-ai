import chess
from chessai.evaluation import evaluate_material, evaluate_mobility

def evaluate(board: chess.Board, color: chess.Color):
    return (evaluate_material(board, color) + evaluate_mobility(board, color)) / 2 


def alphabeta(board: chess.Board, depth: int, color: chess.Color, alpha=-float('inf'), beta=float('inf')):
    if depth == 0 or board.is_game_over():
        return evaluate(board, color), None

    best_move = None
    best_score = -float('inf') if board.turn == color else float('inf')
        
    for move in board.legal_moves:
        # Make the move
        board.push(move)
        score, _ = alphabeta(board, depth - 1, color, alpha, beta)
        board.pop()
        
        # Maximizing the score 
        if board.turn == color:
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, score)
            
        # Minimizing the score
        else:
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, score)

        # Pruning
        if alpha >= beta:
            break
    return best_score, best_move
