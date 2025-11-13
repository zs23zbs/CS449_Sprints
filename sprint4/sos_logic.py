from board_class import Board
from player_class import ComputerPlayer
from abc import ABC, abstractmethod

# Must refactor!

class SOSLogic(ABC):
    def __init__(self, game_board_size, player_blue, player_red):
        """Initialize instance for logic of game"""
        self.board = Board(game_board_size)
        self.player_blue = player_blue 
        self.player_red = player_red
        self.current_turn = player_blue # reconsidering
        self.score_count = {self.player_blue.color : 0, self.player_red.color: 0} # sets the initial score to zero 
    
        self.is_game_over = False
        self.game_mode = ""
    
    @abstractmethod
    def check_game_over(self):
        pass
    
    @abstractmethod
    def determine_winner(self):
        pass
    
    def making_move(self, row, col, letter):
        """Players make a move on board and establish the game's current state"""
        pass

    def during_computers_turn(self):
        """Checks conditions on computers turn, making a move, checking if computer wins"""
        pass

    def switch_turn():
        pass

    def reset_board(self):
        """Resets the game board"""
        self.board.reset() # reset the game board 
        self.current_turn = self.player_blue # automatically set the current player to blue 
        self.score_count = {self.player_blue.color : 0, self.player_red.color: 0} # reset the score count 
        self.is_game_over = False

class SimpleMode(SOSLogic):
    pass

class GeneralMode(SOSLogic):
    pass