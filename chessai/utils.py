import chess

def display_board(board: chess.Board):
    board_str = str(board.unicode(empty_square="."))
    rows = board_str.split('\n')
    print("  +-----------------+")
    for i, row in enumerate(rows):
        print(f"{8 - i} | {row} |")
    print("  +-----------------+")
    print("    a b c d e f g h")
    