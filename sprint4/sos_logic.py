from board_class import Board
from player_class import Player
from abc import ABC, abstractmethod

# Must refactor!

class SOSLogic(ABC):
    def __init__(self, game_board_size, player_blue, player_red):
        """Initialize instance for logic of game"""
        self.board = Board(game_board_size)
        self.player_blue = player_blue 
        self.player_red = player_red
        self.current_turn = player_blue
        self.score_count = {self.player_blue.color : 0, self.player_red.color: 0}
    
        self.is_game_over = False
        self.game_mode = ""
    
    @abstractmethod
    def check_game_over(self):
        pass
    
    @abstractmethod
    def determine_winner(self):
        pass