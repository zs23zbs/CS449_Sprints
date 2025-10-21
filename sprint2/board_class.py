class Board:
    def __init__(self, board_size):
        """Initializes a  2d nested list board with the input board size by user
        
        Args: 
        board_size (int): Integer for the size of the board game
        
        Return: 
            2D Nested List (str): List container for how big the board game will be"""

        self.board_size = board_size
        
        self.game_board = []
        for i in range(board_size): 
            row = []
            for j in range(board_size):
                row.append(None)
            self.game_board.append(row)
    
    def is_cell_empty(self, row, col):
        """Check is board cell is empty 
        
        Args:
        row (int): Row index for where a board seel is on the game board 
        col (int): Column index for where a board seel is on the game board 
        
        Returns: 
            bool: True is the cell is empty, False otherwise 
            """
        
        if self.game_board[row][col] == None:
            return True
        else:
            return False

    def place(self, row, col, letter, color): 
        """Place a letter on the board
        
        Args:
        row (int): Row index for where the letter is placed 
        col (int): Column index for where the letter is placed
        letter (str): The letter to be placed (S or O)
        color (str): Players color (Red or Blue )
        
        Returns: 
            bool: True is the move was successful, False otherwise """
        
        if row not in range(0, self.board_size) or col not in range(0, self.board_size):
            return False
        
        if not self.is_cell_empty(row, col): 
            return False
        
        self.game_board[row][col] = letter, color 

        return True 

    def reset(self):
        """Reset the game if user wishes to do so"""
        self.game_board = []
        for i in range(self.board_size): 
            row = []
            for j in range(self.board_size):
                row.append(None)
            self.game_board.append(row)