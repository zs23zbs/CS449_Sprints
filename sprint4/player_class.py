"""Need to refactor Player Class to include Human and Computer Player"""
from abc import ABC, abstractmethod
from board_class import Board

class Player(ABC):
    def __init__(self, color):
        """Initialize Player objects
        
        Args: 
        color (str): The color for identifying players (Red or Blue)
        """
    
        self.color = color

    @abstractmethod
    def next_move(self, board, available_moves):
        pass 

class HumanPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    def next_move(self, board, available_moves):
        # For now, Handle_click function in GUI should handle human moves 
        return None
        
class ComputerPlayer(Player):
    def __init__(self, color):
        super().__int__(color)

    def next_move(self, board):
        """Looks through the current state of game board and make a valid move"""
        available_moves = [] # store the moves (tuple of cell and letter) that the computer player can make

        # Iterate through all the rows and columns of board game 
        for row in board:
            for col in board:
                # if the cell in board is empty, make cell available for a move
                if Board.is_cell_empty(row, col) == None: 
                    available_moves.append(row, col, "S")
                    available_moves.append(row, col, "O")