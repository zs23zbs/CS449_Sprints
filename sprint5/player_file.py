# Must refactor before implementing Sprint5 
# Follow Basic Refactoring Principles 
from abc import ABC, abstractmethod
from board_file import Board
import random

class Player(ABC):
    def __init__(self, color):
        """Initialize Player objects
        
        Args: 
        color (str): The color for identifying players (Red or Blue)
        """
    
        self.color = color

    @abstractmethod
    def get_move(self, board):
        pass 

class HumanPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board):
        # Handle_click function in GUI handles human moves 
        return None
        
class ComputerPlayer(Player):
    def __init__(self, color):
        super().__init__(color)
    
    def get_move(self, board): # Simplified method for refactoring
        """Looks through the current state of game board and make a valid move"""   
        winning_move = self._find_winning_move(board) 
        if winning_move:
            return winning_move 
        return self._find_random_move(board)
    
    def _find_winning_move(self, board): # Created a private method 
        # Iterate through all the rows and columns of board game 
        for row in range(board.board_size):
            for col in range(board.board_size):
                if board.is_cell_empty(row, col): 

                    # Immediate win strategy 
                    for letter in ["S", "O"]:
                        board.place(row, col, letter, self.color)
                        lines = board.check_for_SOS(row, col)
                        board.unplace(row, col) 
                        if len(lines) > 0: 
                            return (row, col, letter)
    
    def _find_random_move(self, board): 
        available_moves = [] # store the moves (tuple of cell and letter) that the computer player can make

        # Random strategy 
        for row in range(board.board_size):
            for col in range(board.board_size):
                if board.is_cell_empty(row, col):
                    available_moves.append((row, col, "S"))
                    available_moves.append((row, col, "O"))
       
        # computer selects a random avialable spot to make a move on 
        if available_moves:
            computer_move = random.choice(available_moves) 
            return computer_move
        else:
            return None
   