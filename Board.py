class Board:
    def __init__(self, board):
        self.board = board

    def place_card(self, obj, x, y):
        self.board[x][y] = obj