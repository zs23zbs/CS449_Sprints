"""Need to refactor Player Class to include Human and Computer Player"""
from abc import ABC, abstractmethod
from board_class import Board
import random

class Player(ABC):
    def __init__(self, color):
        """Initialize Player objects
        
        Args: 
        color (str): The color for identifying players (Red or Blue)
        """
    
        self.color = color

    @abstractmethod
    def next_move(self, board):
        pass 

class HumanPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    def next_move(self, board):
        # For now, Handle_click function in GUI should handle human moves 
        return None
        
class ComputerPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    def next_move(self, board):
        """Looks through the current state of game board and make a valid move"""
        available_moves = [] # store the moves (tuple of cell and letter) that the computer player can make

        # Iterate through all the rows and columns of board game 
        for row in range(board.board_size):
            for col in range(board.board_size):
                # if the cell in board is empty, make cell available for a move
                if board.is_cell_empty(row, col): 
                    available_moves.append((row, col, "S"))
                    available_moves.append((row, col, "O"))

        if available_moves: # if the board is full
            computer_move = random.choice(available_moves) # computer selects a random avialable spot to make a move on 
            return computer_move
        else:
            return None # the board is full 