import chess
import chess.engine
from chessai.utils import display_board
from chessai.minimax import minimax
from chessai.alphabeta import alphabeta

def player_move(board: chess.Board):
    """
    Get a move from the player via console input.
    """
    move = None
    while move not in board.legal_moves:
        user_input = input("Enter your move in UCI format (e.g., e2e4): ")
        try:
            move = chess.Move.from_uci(user_input)
            if move not in board.legal_moves:
                print("Illegal move, try again.")
        except ValueError:
            print("Invalid input, try again.")
    return move

def engine_move(board: chess.Board, engine_path: str, time_limit: float = 1.0):
    """
    Get a move from a chess engine.
    """
    with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
        result = engine.play(board, chess.engine.Limit(time=time_limit))
        return result.move

def main(p1: str, p2: str, depth: int = 3):
    """
    Main function to run the chess game with different modes.

    Args:
        p1 (str): Player 1 type ('player', 'minimax', 'alphabeta', 'engine').
        p2 (str): Player 2 type ('player', 'minimax', 'alphabeta', 'engine').
        depth (int): Search depth for minimax and alphabeta.
    """
    board = chess.Board()

    while not board.is_game_over():
        display_board(board)

        if board.turn == chess.WHITE:
            if p1 == 'player':
                move = player_move(board)
            elif p1 == 'minimax':
                _, move = minimax(board, depth, True)
            elif p1 == 'alphabeta':
                _, move = alphabeta(board, depth, chess.WHITE)
            elif p1 == 'engine':
                move = engine_move(board, 'path/to/engine')
            else:
                raise ValueError("Invalid player type for p1")
        else:
            if p2 == 'player':
                move = player_move(board)
            elif p2 == 'minimax':
                _, move = minimax(board, depth, False)
            elif p2 == 'alphabeta':
                _, move = alphabeta(board, depth, chess.BLACK)
            elif p2 == 'engine':
                move = engine_move(board, 'path/to/engine')
            else:
                raise ValueError("Invalid player type for p2")

        board.push(move)

    print(board.unicode(empty_square="."))
    result = board.result()
    print(f"Game over: {result}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run a chess game with different modes.")
    parser.add_argument("p1", type=str, choices=['player', 'minimax', 'alphabeta', 'engine'], help="Player 1 type")
    parser.add_argument("p2", type=str, choices=['player', 'minimax', 'alphabeta', 'engine'], help="Player 2 type")
    parser.add_argument("--depth", type=int, default=3, help="Search depth for minimax and alphabeta")

    args = parser.parse_args()

    main(args.p1, args.p2, args.depth)
