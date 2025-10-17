"""Board Class"""
# Represents the grid (2d list of cells)
# Keep track of what is in the ceels (S or O, or empty) 
# Ensure valid moves

class Board:
    def __init__(self, board_size): #===Works!===
        # Initializes a  2d nested list board with the input board size by user 
        self.board_size = board_size
        
        self.game_board = []
        for i in range(board_size): 
            row = []
            for j in range(board_size):
                row.append(None)
            self.game_board.append(row)
    
    def is_cell_empty(self, row, col):  #===Works!===
        # Before player makes a move on cell, system checks if it is empty 
        if self.game_board[row][col] == None:
            return True
        else:
            return False

    def place(self, row, col, letter, color): #===Works!===
        # Updates the cell whichever player chooses to make a move
        if row not in range(0, self.board_size) or col not in range(0, self.board_size):
            return False
        
        if not self.is_cell_empty(row, col): 
            return False
        
        self.game_board[row][col] = letter, color 

        return True 

    def reset(self): #===Check===
        #Reset the the board, all cells are empty once more
        self.game_board = []
        for i in range(self.board_size): 
            row = []
            for j in range(self.board_size):
                row.append(None)
            self.game_board.append(row)
