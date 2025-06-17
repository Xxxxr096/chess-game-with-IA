def pawn_moves(board, row, col, color):
    moves = []
    direction = -1 if color == "white" else 1
    start_row = 6 if color == "white" else 1

    # 1. Case devant (1 case)
    if 0 <= row + direction < 8 and board[row + direction][col] is None:
        moves.append((row + direction, col))

        # 2. 2 cases devant depuis la ligne de départ
        if row == start_row and board[row + 2 * direction][col] is None:
            moves.append((row + 2 * direction, col))

    # 3. Captures diagonales
    for dc in [-1, 1]:
        new_col = col + dc
        new_row = row + direction
        if 0 <= new_col < 8 and 0 <= new_row < 8:
            target = board[new_row][new_col]
            if target and target.color != color and target.name != "k":
                moves.append((new_row, new_col))

    return moves


def rock_moves(board, row, col, color):
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc

        while 0 <= r < 8 and 0 <= c < 8:
            target = board[r][c]
            if target is None:
                moves.append((r, c))
            elif target.color != color and target.name != "k":
                moves.append((r, c))
                break
            else:
                break

            r += dr
            c += dc
    return moves


def knight_moves(board, row, col, color):
    moves = []
    directions = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < 8 and 0 <= c < 8:
            target = board[r][c]
            if target is None or target.color != color and target.name != "k":
                moves.append((r, c))
    return moves


def bishop_moves(board, row, col, color):
    moves = []
    direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    for dr, dc in direction:
        r, c = row + dr, col + dc
        while 0 <= r < 8 and 0 <= c < 8:
            target = board[r][c]
            if target == None:
                moves.append((r, c))
            elif target.color != color and target.name != "k":
                moves.append((r, c))
                break
            else:
                break
            r += dr
            c += dc
    return moves


def queen_moves(board, row, col, color):
    moves = []
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    for dr, dc in direction:
        r, c = row + dr, col + dc
        while 0 <= r < 8 and 0 <= c < 8:
            target = board[r][c]
            if target == None:
                moves.append((r, c))
            elif target.color != color and target.name != "k":
                moves.append((r, c))
                break
            else:
                break
            r += dr
            c += dc
    return moves


def king_moves(board, row, col, color):
    moves = []
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),  # diagonale haut-gauche, haut, haut-droite
        (0, -1),
        (0, 1),  # gauche,         , droite
        (1, -1),
        (1, 0),
        (1, 1),  # diagonale bas-gauche, bas, bas-droite
    ]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < 8 and 0 <= c < 8:
            target = board[r][c]
            if target is None or target.color != color and target.name != "k":
                moves.append((r, c))
    return moves
