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

    def place(self, row, col, letter, color):
        """Place a ltter on the game board"""
        if not self.is_cell_empty(row, col):
            return False
        
        self.game_board[row][col] = (letter, color)

        return True 

    def get_letter(self, row, col):
        """Returns the letter (S or O) from a cell or None"""
        if 0 <= row < self.board_size and 0 <= col < self.board_size:
            content = self.game_board[row][col]
            if content is not None: # if the cell is not empty 
                return content[0] # take the letter from tuple (letter, color)
        return None
    
    # Refactored, but doubtful 
    def check_for_SOS(self, row, col):
        """Detects an SOS and return line coordinates"""
        directions = [
            (-1, 0), (1, 0),  # Vertical (N, S)
            (0, -1), (0, 1),  # Horizontal (W,E)
            (-1, -1), (1, 1), # Diagonal 1 (NW, SE)
            (-1, 1), (1, -1) # Diagonal 2 (NE, SW) 
        ]
  
        newly_found_lines = [] 
        current_letter = self.get_letter(row, col)
        players_color = self.game_board[row][col][1] # get whichever players color 

        for rd, cd in directions: # row direction = rd, cd = column direction

            # when O is in the middle (S - O - S)
            if current_letter == "O":
                s1_r, s1_c = (row - rd), (col- cd)
                s2_r, s2_c = (row + rd), (col + cd)
                s1 = self.get_letter(s1_r, s1_c)
                s2 = self.get_letter(s2_r, s2_c)

                if s1 == "S" and s2 == "S": 
                    line_tuple1 = ((s1_r, s1_c), (row, col), (s2_r, s2_c))
                    newly_found_lines.append({"line": line_tuple1, "color": players_color})
            
            # when S is the first or last (S - O - S)
            if current_letter == "S":
                # S (new) - O - S
                o1_r, o1_c = (row + rd), (col + cd)
                s1_r, s1_c = row + ( 2 * rd), col + (2 * cd)
                o1 = self.get_letter(o1_r, o1_c)
                s1 = self.get_letter(s1_r, s1_c)

                if o1 == "O" and s1 == "S":
                    line_tuple2 = ((row, col), (o1_r, o1_c), (s1_r, s1_c))
                    newly_found_lines.append({"line": line_tuple2, "color": players_color})

            
                # S - O - S (new)
                s2_r, s2_c = row - (2 * rd), col - (2* cd)
                o2_r, o2_c = (row - rd), (col - cd)
                s2 = self.get_letter(s2_r, s2_c)
                o2 = self.get_letter(o2_r, o2_c)

                if s2 == "S" and o2 == "O":
                    line_tuple3 = ((s2_r, s2_c), (o2_r, o2_c), (row, col))
                    newly_found_lines.append({"line": line_tuple3, "color": players_color})

        return newly_found_lines
    
    def reset(self):
        """Resets the game board, all cells empty"""
        self.game_board = []
        for i in range(self.board_size): 
            row = []
            for j in range(self.board_size):
                row.append(None)
            self.game_board.append(row)
    
    def is_full(self):
        """Checks if the game board is filled"""
        for row in self.game_board:
            if None in row:
                return False
        return True 