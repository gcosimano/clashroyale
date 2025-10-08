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


    def __init__(self, length=18, width=29):
        # Initialize the 2D array using nested list comprehensions:
        # Outer loop controls the rows (length/X)
        # Inner loop controls the columns (width/Y)
        self.board = [
            [None for _ in range(width)] 
            for _ in range(length)
        ]

        #placing Towers on their appropriate squares
        #princess L computer -----col=y (4,7), row=x (2,4)
        for r in range(2,5):
            for c in range(4,8):
                self.board[r][c] = princess_L_computer
        
        #princess R computer ----y(4,7), x(13,15)
        for r in range(13,16):
            for c in range(4,8):
                self.board[r][c] = princess_R_computer

        #princess L user  
        for r in range(2,5):
            for c in range(21,25):
                self.board[r][c] = princess_L_user

        #princess R user
        for r in range(13,16):
            for c in range(21,25):
                self.board[r][c] = princess_R_user

        #king computer
        for r in range(7,11):
            for c in range(0,5):
                self.board[r][c] = king_computer

        #king user
        for r in range(7,11):
            for c in range(24,29):
                self.board[r][c] = king_user   

    
    
    def place_card(self, card, x, y):
        if self.board[x][y] is None
            self.board[x][y] = card
            card.setPos(x, y)
            pos = [x, y]
            card.path_list.append(pos)
        else
            return False

# Creates 18x32 game board array
print("x")
board = Board()


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