"""Need to refactor Player Class to include Human and Computer Player"""
from abc import ABC, abstractmethod

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