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
        
        current_player_color = self.current_turn.color # get the which players color turn is it 
        valid_move = self.board.place(row, col, letter, current_player_color) # current player makes a valid move 

        # if current players move make an SOS
        if valid_move:
            found_sos = self.board.check_for_SOS(row, col) #checks if a sos pattern was found 
            score_made = len(found_sos) > 0 # capture the score amount with each sos pattern found 

        # increment current player who scored with an sos pattern 
        


    def during_computers_turn(self):
        """Checks condition on computers turn, making a move, checking if computer wins"""
        pass

    def switch_turn(self):
        """Switch turns between players after each move"""
        if self.current_turn == self.player_blue: 
            self.current_turn = self.player_red
        else: 
            self.current_turn = self.player_blue

    def reset_board(self):
        """Resets the game board"""
        self.board.reset() # reset the game board 
        self.current_turn = self.player_blue # automatically set the current player to blue 
        self.score_count = {self.player_blue.color : 0, self.player_red.color: 0} # reset the score count for players 
        self.is_game_over = False

class SimpleMode(SOSLogic):
    def __init__(self, game_board_size):
        super().__init__(game_board_size)

    def check_game_over(self):
        pass

    def determine_winner(self):
        pass

class GeneralMode(SOSLogic):
    def __init__(self, game_board_size):
        super().__init(game_board_size)
    
    def check_game_over(self):
        pass
    
    def determine_winner(self):
        pass