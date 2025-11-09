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
    pass
        

class ComputerPlayer(Player):
    pass