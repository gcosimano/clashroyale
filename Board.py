class Board:
    def __init__(self, length=18, width=32):
        # Initialize the 2D array using nested list comprehensions:
        # Outer loop controls the rows (length/X)
        # Inner loop controls the columns (width/Y)
        self.board = [
            [None for _ in range(width)] 
            for _ in range(length)
        ]

# Creates 18x32 game board array
board = Board()


'''
    def place_card(self, obj, x, y):
        self.board[x][y] = obj
        obj.setPos(x, y)
        print(f"x: {x} y: {y}")

# 18x32
# create a 2D array to represent the board
# place towers on board (make sure each point of the tower points to the same object)
# place paths on board
# place rivers/bridges on board
# place card method for x and y
# card automatically goes to left or right bridge depending on which is closer
# if card is place on y coord below or equal to towers, it goes straight up past them, diagonal to path, and straight up path
'''