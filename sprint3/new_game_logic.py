from new_board_class import Board
from new_player_class import Player
from abc import ABC, abstractmethod

class SOSGameLogic(ABC):
    def __init__(self, game_board_size):
        """Initialize instance for logic of game"""
        self.board = Board(game_board_size)
        self.player_blue = Player("Blue")
        self.player_red = Player("Red")
        self.current_turn = self.player_blue
        self.SOS_count = {self.player_blue.color : 0, self.player_red.color : 0} # Start the score coun for each player when game beings

        self.is_game_over = False
        self.game_mode_name = ""

    @abstractmethod
    def check_game_over(self):
        pass
    
    @abstractmethod
    def determine_winner(self):
        pass