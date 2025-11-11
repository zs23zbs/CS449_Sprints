class Board():
    def __init__(self, board_size):
        """Initiate the 2d nested list for board"""
        self.board_size = board_size
        self.game_board = []
        for i in range(board_size): 
            row = []
            for j in range(board_size):
                row.append(None)
            self.game_board.append(row)

    def is_cell_empty(self, row, col):
        """Checks if board cell is empty and checks boundaries"""
        if not (0 <= row < self.board_size and 0 <= col < self.board_size):
            return False
        return self.game_board[row][col] is None 