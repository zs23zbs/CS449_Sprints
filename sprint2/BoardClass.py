"""Board Class"""
# Represents the grid (2d list of cells)
# Keep track of what is in the ceels (S or O, or empty) 
# Ensure valid moves 
# Is a provided helper funtion for logic and GUI 

class Board:
    def __init__(self, board_size): 
        # Initializes a  2d nested list board with the input board size by user 
        self.board_size = board_size
        
        self.game_board = []
        for i in range(board_size): 
            row = []
            for j in range(board_size):
                row.append(None)
            self.game_board.append(row)
    
    def is_cell_empty(self, row, col): 
        # Before player makes a move on cell, system checks if it is empty 
        if self.game_board[row][col] == None:
            return True
        else:
            return False

    def place(self, row, col, letter, color): 
        # Updates the cell whichever player chooses to make a move
        if row not in range(0, self.board_size) or col not in range(0, self.board_size):
            return False
        
        if not self.is_cell_empty(row, col): 
            return False
        
        self.game_board[row][col] = letter

        return True 

    def reset(self): #Reset the the board, all cells are empty once more
        
        self.game_board = []
        for i in range(self.board_size): 
            row = []
            for j in range(self.board_size):
                row.append(None)
            self.game_board.append(row)
        

    def __str__(self): #Just to be able to see the board itself
        return f"{self.game_board}" 

new_game_board = Board(3)

print(new_game_board.game_board)