from Card import Card
from Tower import Tower, KingTower
import time

class Board:

    

    def __init__(self, length=32, width=18, elapsed=0):
        # Initialize the 2D array using nested list comprehensions:
        # Outer loop controls the rows (length/X)
        # Inner loop controls the columns (width/Y)

        self.elapsed = elapsed
        self.length = length
        self.width = width

        self.board = [
            [None for _ in range(width)] 
            for _ in range(length)
        ]

        #creating towers to go into board array, level 1 towers
        self.princess_L_user = Tower(50, 7.5, 2400, False, True)
        self.princess_R_user = Tower(50, 7.5, 2400, False, True)
        self.princess_L_computer = Tower(50, 7.5, 2400, False, False)
        self.princess_R_computer = Tower(50, 7.5, 2400, False, False)
        self.king_user = KingTower(50, 7, 2400, False, False, True)
        self.king_computer = KingTower(50, 7, 2400, False, False, False)
        self.river = Card(-1, 0, "River", {}, 0, [], [], False, False, False, False)

        #placing Towers on their appropriate squares
        #princess L computer -----col=y (2,4), row=x (5,7)
        for r in range(5,8):
            for c in range(2,5):
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
        for r in range(24,27):
            for c in range(13,16):
                self.board[r][c] = self.princess_R_user

        #king computer ---- y(7,10), x(1,4)
        for r in range(1,5):
            for c in range(7,11):
                self.board[r][c] = self.king_computer

        #king user ---- y(7,10), x(27,30)
        for r in range(27,31):
            for c in range(7,11):
                self.board[r][c] = self.king_user   


        for r in range(15, 17):
            for c in range(0,18):
                self.board[r][c] = self.river


    def print_board(self):
        # Determine board dimensions
        num_rows = len(self.board)
        num_cols = len(self.board[0])
        
        # --- 1. Print Column Headers (Top) ---
        
        # Print a blank space (or header) to align with the row indices
        # We use a placeholder to ensure alignment with the row index numbers (0-30)
        # We also use str(num_rows) to dynamically create the correct spacing.
        print(" " * (len(str(num_rows))) + " ", end="") 
        
        # Print the column indices (0, 1, 2, ... 16)
        for c in range(num_cols):
            # Print column index followed by a space
            print(f"{c: <2}", end=" ") # Use f-string for 2-digit minimum width formatting
        print() # Newline after the column headers
        
        # --- 2. Print Each Row with its Index (Side) ---
        
        # Use enumerate to get both the index (r) and the row content
        for r, row in enumerate(self.board):
            # Print the row index (r) followed by a colon for visual separation
            print(f"{r: <{len(str(num_rows))}}:", end=" ") 
            
            row_elements = []
            for item in row:
                # Use the same logic as before for element representation
                if isinstance(item, KingTower):
                    if item.is_user == True:
<<<<<<< HEAD
                        row_elements.append('K')
                    else:
                        row_elements.append('k') 
                # add color logic for each if statement
                elif isinstance(item, Tower):
                    if item.is_user == True:
                        row_elements.append('P')
                    else:
                        row_elements.append('p') 
=======
                         row_elements.append("\033[34mK\033[0m") 
                    else:
                        row_elements.append("\033[31mk\033[0m") 
                elif isinstance(item, Tower):
                    if item.is_user == True:
                        row_elements.append("\033[34mP\033[0m") 
                    else:
                        row_elements.append("\033[31mp\033[0m") 
>>>>>>> fd25bb4ba2a309edf00dba1be659203f60be398a
                elif item is None:
                    row_elements.append(".")
                elif item is (self.river):
<<<<<<< HEAD
                    row_elements.append('~')
=======
                    row_elements.append("\x1b[94m~\x1b[0m")
>>>>>>> fd25bb4ba2a309edf00dba1be659203f60be398a
                else:
                    # For a Card or other object
                    row_elements.append('O')
            
            # Print the row contents
            print("  ".join(row_elements))

    
    

# 1/60 fps?
    # need to add smthing to make sure the coords aren't out of bounds
    def place_card(self, obj: Card, x, y):
        obj.time_since_moved = self.elapsed
        self.board[x][y] = obj
        obj.setPos(x, y)
        print(f"x: {x} y: {y}")

    def move_card(self, obj: Card):
        # check area of sight/determine target - DO LATER
        #if something is in target, move towards it - DO LATER
        #if u can shoot at it, shoot at it - DOLATER
        #remove where it was before
        if self.elapsed == obj.time_since_moved + 1:
            obj1 = self.board[obj.x][obj.y]
            obj1.setPos(obj.x, obj.y + obj.speed)
            self.board[obj.x][obj.y] = None
        


    def measure_elapsed_time(self):
        start_time = time.monotonic()        

        while True:
            current_time = time.monotonic()
            new_elapsed = round((current_time - start_time),1)
            if new_elapsed > self.elapsed:
                self.elapsed = new_elapsed
                # print(self.elapsed, "seconds have elapsed.")
            
            time.sleep(.1)
        

# MAKE TIME INSTANCE VAR

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

