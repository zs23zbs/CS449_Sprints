from new_player_class import Player # imports from Player class

class Board():
    def __intit__(self, board_size):
        """Initiate the 2d nested list for board"""
        self.board_size = board_size
        self.game_board = [[None] * board_size for _ in range(board_size)] # create the 2d nested lists depending on the value for board_size 
    
    def is_cell_empty(self, row, col):
        """Checks if board cell is empty and checks boundaries"""
        if not (0 <= row < self.board_size and 0 <= col < self.board_size): # if not within bounds 
            return False
        return self.game_board[row][col] is None 
    
    def get_letter(self, row, col):
        """Returns the letter (S or O) from a cell or None"""
        if 0 <= row < self.board_size and 0 <= col < self.board_size:
            content = self.game_board[row][col]
            if content is not None: # if the cell is not empty 
                return content[0] # store tuple (letter, color)
        return None
    