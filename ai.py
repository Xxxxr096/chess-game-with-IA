import random


def get_all_legal_moves(board, color):
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board.board[row][col]
            if piece and piece.color == color:
                legal = board.get_legal_moves(row, col)
                for move in legal:
                    moves.append(((row, col), move))
    return moves


def play_random_move(board, color):
    moves = get_all_legal_moves(board, color)
    if moves:
        start, end = random.choice(moves)
        board.move_piece(start, end)
