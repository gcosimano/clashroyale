from Card import Card
from Tower import Tower, KingTower

class Board:
    #creating towers to go into board array, level 1 towers
    princess_L_user = Tower.Tower(50, 7.5, 2400, False)
    princess_R_user = Tower.Tower(50, 7.5, 2400, False)
    princess_L_computer = Tower.Tower(50, 7.5, 2400, False)
    princess_R_computer = Tower.Tower(50, 7.5, 2400, False)
    king_user = Tower.KingTower(50, 7, 2400, False, False)
    king_computer = Tower.KingTower(50, 7, 2400, False, False)


    def __init__(self, length=31, width=17):
        # Initialize the 2D array using nested list comprehensions:
        # Outer loop controls the rows (length/X)
        # Inner loop controls the columns (width/Y)
        self.board = [
            [None for _ in range(width)] 
            for _ in range(length)
        ]

        #placing Towers on their appropriate squares
        #princess L computer -----col=y (2,4), row=x (5,7)
        for r in range(5,8):
            for c in range(2,9):
                self.board[r][c] = self.princess_L_computer
        
        #princess R computer ----y(5,7), x(13,15)
        for r in range(5,8):
            for c in range(13,16):
                self.board[r][c] = self.princess_R_computer

        #princess L user ----y(24,26), x(2,4)
        for r in range(24,27):
            for c in range(2,5):
                self.board[r][c] = self.princess_L_user

        #princess R user ----y(24,26), x(13,15)
        for r in range(13,16):
            for c in range(24,27):
                self.board[r][c] = self.princess_R_user

        #king computer ---- y(7,10), x(1,4)
        for r in range(1,5):
            for c in range(7,11):
                self.board[r][c] = self.king_computer

        #king user ---- y(7,10), x(27,30)
        for r in range(27,31):
            for c in range(7,11):
                self.board[r][c] = self.king_user   


# need to add smthing to make sure the coords aren't out of bounds
def place_card(self, obj, x, y):
    self.board[x][y] = obj
    obj.setPos(x, y)
    print(f"x: {x} y: {y}")


'''
# 18x32
# create a 2D array to represent the board
# place towers on board (make sure each point of the tower points to the same object)
# place paths on board
# place rivers/bridges on board
# place card method for x and y
# card automatically goes to left or right bridge depending on which is closer
# if card is place on y coord below or equal to towers, it goes straight up past them, diagonal to path, and straight up path
'''

