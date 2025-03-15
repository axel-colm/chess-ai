import chess

MAX_MATERIAL = 39
PIECES_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
}

def evaluate_material(board: chess.Board, player: chess.Color) -> float:
    # Check for checkmate
    if board.is_checkmate():
        return -9999 if board.turn == player else 9999
    if board.is_game_over():
        return -9999
    
    occupied_squareset = chess.SquareSet(board.occupied)
    material = 0
    
    for square in occupied_squareset:
        piece = board.piece_at(square)
        sign = 1 if piece.color == player else -1
        material += sign * PIECES_VALUES[piece.piece_type]
    return material / MAX_MATERIAL
    
    
MAX_LEGAL_MOVES = 218
def evaluate_mobility(board: chess.Board, player: chess.Color) -> float:
    legal_moves = len(list(board.legal_moves))
    return legal_moves / MAX_LEGAL_MOVES