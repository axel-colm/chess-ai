import chess

def evaluate_material(board: chess.Board, player: chess.Color) -> float:
    if board.is_checkmate():
        if board.turn == player:
            return -9999
        else:
            return 9999
    elif board.is_stalemate() or board.is_insufficient_material():
        return 0

    eval = 0
    values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9
    }
    for piece_type, value in values.items():
        eval += value * len(board.pieces(piece_type, player))
        eval -= value * len(board.pieces(piece_type, not player))
    return eval
