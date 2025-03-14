import chess
from chessai.evaluation import evaluate_material, evaluate_mobility

def evaluate(board: chess.Board, color: chess.Color):
    return evaluate_material(board, color) + evaluate_mobility(board, color)

def sort_moves(board: chess.Board):
    """
    Sort moves based on heuristics: captures, checks, promotions, mobility.
    """
    def move_value(move):
        if board.is_capture(move):
            return 4
        if board.gives_check(move):
            return 3
        if board.piece_type_at(move.from_square) == chess.PAWN and chess.square_rank(move.to_square) in [0, 7]:
            return 2
        return 1

    return sorted(board.legal_moves, key=move_value, reverse=True)

def alphabeta(board: chess.Board, depth: int, color: chess.Color, alpha=-float('inf'), beta=float('inf')):
    if depth == 0 or board.is_game_over():
        return evaluate(board, color), None

    best_score = -float('inf') if color == chess.WHITE else float('inf')
    best_move = None

    for move in sort_moves(board):
        board.push(move)
        score, _ = alphabeta(board, depth - 1, not color, alpha, beta)
        board.pop()

        if color == chess.WHITE:
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, score)
        else:
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, score)

        if alpha >= beta:
            break

    return best_score, best_move
