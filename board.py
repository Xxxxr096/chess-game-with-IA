from pieces import Piece
from game_logic import (
    pawn_moves,
    rock_moves,
    knight_moves,
    bishop_moves,
    queen_moves,
    king_moves,
)
import pygame

ROWS, COLS = 8, 8


class Board:
    def __init__(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.setup_pieces()

    def setup_pieces(self):
        # Pawns
        for i in range(COLS):
            self.board[1][i] = Piece("p", "black")
            self.board[6][i] = Piece("p", "white")

        # Rook
        self.board[0][0] = Piece("r", "black")
        self.board[0][7] = Piece("r", "black")

        self.board[7][0] = Piece("r", "white")
        self.board[7][7] = Piece("r", "white")

        # knight
        self.board[0][1] = Piece("n", "black")
        self.board[0][6] = Piece("n", "black")

        self.board[7][1] = Piece("n", "white")
        self.board[7][6] = Piece("n", "white")

        # Bishop
        self.board[0][2] = Piece("b", "black")
        self.board[0][5] = Piece("b", "black")

        self.board[7][2] = Piece("b", "white")
        self.board[7][5] = Piece("b", "white")

        # king
        self.board[0][3] = Piece("k", "black")
        self.board[7][3] = Piece("k", "white")

        # Queen
        self.board[0][4] = Piece("q", "black")
        self.board[7][4] = Piece("q", "white")

    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]

        # Déplacer la piéce si une piéce est selectionné
        if piece:
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = None

    def get_legal_moves(self, row, col):
        piece = self.board[row][col]
        if not piece:
            return []
        if piece.name == "p":
            return pawn_moves(self.board, row, col, piece.color)
        if piece.name == "r":
            return rock_moves(self.board, row, col, piece.color)
        if piece.name == "n":
            return knight_moves(self.board, row, col, piece.color)
        if piece.name == "b":
            return bishop_moves(self.board, row, col, piece.color)
        if piece.name == "q":
            return queen_moves(self.board, row, col, piece.color)
        if piece.name == "k":
            return king_moves(self.board, row, col, piece.color)
        return []

    def draw(self, win, images, legal_moves=[]):
        colors = [pygame.Color("white"), pygame.Color("gray")]
        for row in range(ROWS):
            for col in range(COLS):
                color = colors[(row + col) % 2]
                pygame.draw.rect(win, color, (col * 80, row * 80, 80, 80))

                if (row, col) in legal_moves:
                    s = pygame.Surface((80, 80), pygame.SRCALPHA)
                    s.fill((0, 255, 0, 80))  # vert transparent
                    win.blit(s, (col * 80, row * 80))
                if (row, col) in legal_moves and self.board[row][col] != None:
                    s.fill((139, 0, 0, 100))
                    win.blit(s, (col * 80, row * 80))
                piece = self.board[row][col]
                if piece:
                    img_key = piece.color[0] + piece.name
                    win.blit(images[img_key], (col * 80, row * 80))
