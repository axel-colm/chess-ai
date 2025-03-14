import chess

def evaluate_material(board: chess.Board, player: chess.Color) -> float:
    """
    Evaluate the material on the board for the given player.
    Each piece is assigned a value:
    - Pawn: 1
    - Knight: 3
    - Bishop: 3
    - Rook: 5
    - Queen: 9
    - King: 200
    The evaluation is the sum of the values of the player's pieces minus the sum of the values of the opponent's pieces.
    The evaluation is -9999 if the player is checkmated, 9999 if the opponent is checkmated, and 0 if the game is a stalemate or if there is insufficient material.
    
    Args:
        board (chess.Board): The board to evaluate.
        player (chess.Color): The player for which to evaluate the material.
        
    """
    if board.is_checkmate():
        return -9999 if board.turn == player else 9999
    elif board.is_stalemate() or board.is_insufficient_material():
        return 0
    
    eval = 0
    values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 200
    }
    for piece_type, value in values.items():
        eval += value * len(board.pieces(piece_type, player))
        eval -= value * len(board.pieces(piece_type, not player))
    return eval


def evaluate_mobility(board: chess.Board, player: chess.Color) -> float:
    """
    Evaluate the mobility on the board for the given player.
    The evaluation is the number of legal moves for the player minus the number of legal moves for the opponent.
    
    Args:
        board (chess.Board): The board to evaluate.
        player (chess.Color): The player for which to evaluate the mobility.
        
    """
    board = board.copy()
    eval = 0
    for color in chess.COLORS:
        board.turn = color
        sign = 1 if color == player else -1
        eval += sign * len(list(board.legal_moves))
    return eval
