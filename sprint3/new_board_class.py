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
    
    def get_letter(self, row, col):
        """Checks for safety boundaries
        Returns:
        None, if out of bound or cell is empty"""

        if 0 <= row < self.game_board and 0 <= col < self.game_board:
            content_of_cell = self.game_board[row][col]
            if content_of_cell is not None:
                return content_of_cell[0] # Takes the the first element in tuple (letter, color)
            
        return None

    def check_for_SOS(self, row, col):
        """Detect an SOS in game to determine a winner (Simple Mode) or points (General Mode)
        
        Args: 
        row (int): Row index for where the letter is placed 
        col (int): Column index for where the letter is placed
        
        Returns:
            int: number of SOS lines created 
            """
        
        directions = [
            (-1, 0), (1, 0) # Vertical (N, S)
            (0, -1) , (0, 1) # Horizontal (W, E) 
            (-1, -1) , (1, 1) # Diagonal 1 (NW, SE)
            (-1, 1) , (1, -1) # Diagonal 2 (NE, SW)
        ]
        
        counting_SOS = 0  

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