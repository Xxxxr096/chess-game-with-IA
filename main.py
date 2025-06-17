import pygame
from board import Board

# Init pygame
pygame.init()


WIDTH, HEIGHT = 640, 640
SQUARE_SIZE = WIDTH // 8
FPS = 60

# Init de la fenetre
windows = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu d'échecs")
from ai import play_random_move


# charger les images des piéces
def load_images():
    pieces = ["bb", "bk", "bn", "bp", "bq", "br", "wb", "wk", "wn", "wp", "wq", "wr"]
    images = {}
    for piece in pieces:
        images[piece] = pygame.transform.scale(
            pygame.image.load(f"assets/{piece}.png"), (SQUARE_SIZE, SQUARE_SIZE)
        )
    return images


def main():
    clock = pygame.time.Clock()
    images = load_images()
    board = Board()
    run = True
    selected = None
    legal_moves = []
    turn = "white"

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and turn == "white":
                x, y = pygame.mouse.get_pos()
                col = x // SQUARE_SIZE
                row = y // SQUARE_SIZE

                if selected:
                    if (row, col) in legal_moves:
                        board.move_piece(selected, (row, col))
                        selected = None
                        legal_moves = []
                        turn = "black"

                        # ✅ L'IA joue immédiatement après le joueur blanc
                        play_random_move(board, "black")
                        turn = "white"

                    else:
                        piece = board.board[row][col]
                        if piece and piece.color == "white":
                            selected = (row, col)
                            legal_moves = board.get_legal_moves(row, col)
                        else:
                            selected = None
                            legal_moves = []

                else:
                    piece = board.board[row][col]
                    if piece and piece.color == "white":
                        selected = (row, col)
                        legal_moves = board.get_legal_moves(row, col)

        board.draw(windows, images, legal_moves)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
