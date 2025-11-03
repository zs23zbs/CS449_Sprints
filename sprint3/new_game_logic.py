from new_board_class import Board
from new_player_class import Player
from abc import ABC, abstractmethod

class SOSBaseGameLogic(ABC):
    def __init__(self, game_board_size, mode):
        """Initialize Game Logic objects
        
        Args: 
        game_board_size (int): Size of the board game 
        mode (str): Mode of which the player selects (Simple or General
        
        """
        self.board = Board(game_board_size)

        # Created Objects
        self.player_blue = Player("Blue")
        self.player_red = Player("Red")

        # Start with Blue player's turn 
        self.current_turn = self.player_blue

        # score tracking 
        self.SOS_count = {self.player_red.color : 0, self.player_blue.color : 0}

        # game over flag
        self.is_game_over = False

    @abstractmethod
    def check_for_game_over(self):
        """
        ABSTRACT: Determines if the game ended based on mode rules.
        Will be implemented by SimpleGameLogic and GeneralGameLogic.
        """
        pass

    @abstractmethod
    def determine_winner(self):
        """
        ABSTRACT: Calculates the winner based on mode rules (score, first win, etc.).
        Will be implemented by SimpleGameLogic and GeneralGameLogic.
        """
        pass

    def make_move(self, row, col, letter): 
        """Placing a move on game board 
        
        Args:
        row (int): Row index for the board cells
        col (int): Column index for the board cells 
        
        Return:
            bool: True if the cell is empty, False otherwise 
        """

        if self.board.is_cell_empty(row, col):
            self.board.place(row, col, letter, self.current_turn.color)
            new_SOS_line = self.board.check_for_SOS(row, col)
            if new_SOS_line > 0:
                self.sos_count[self.current_turn.color] += new_SOS_line
        
            self.check_for_game_over() # Calls the abstract method

            if not self.is_game_over and new_SOS_line == 0:
                self.switch_turn()

            return True 
        
        else: 
            return False
        
    def switch_turn(self): 
        """Switch turns between player with each move done"""
        
        if self.current_turn == self.player_blue: 
            self.current_turn = self.player_red
        else:
            self.current_turn = self.player_blue

    def reset(self):
        self.board.reset()
        self.current_turn = self.player_blue

class SimpleMode(SOSBaseGameLogic):
    def __init__(self, game_board_size):
        super().__init__(game_board_size)
        self.game_mode_name = "Simple Game"

    def check_for_game_over(self):
        """Game over if and only if: 
            1) Any player scores first SOS, wins
            2) Board is completely full (draw if no score)
        """

        red_score = self.SOS_count[self.player_red.color]
        blue_score = self.SOS_count[self.player_blue.color]

        is_board_full = self.board.is_full()

        if red_score > 0 or blue_score > 0 or is_board_full:
            self.is_game_over = True

    def determine_winner(self):
        """Simple Mode Rule: First player to put SOS wins"""

        red_score = self.SOS_count[self.player_red.color]
        blue_score = self.SOS_count[self.player_blue.color]

        if red_score > 0 and blue_score  == 0: # if red player wins 
            return self.player_red.color
        if blue_score > 0 and red_score == 0: # if blue player wins 
            return self.player_blue.color
    
        # if both scored at the same time
        return "Draw"

class GeneralMode(SOSBaseGameLogic):
    def __init__(self, game_board_size):
        super().__init__(game_board_size)
        self.game_mode_name = "General Game"

    def check_for_game_over(self):
        """Game is only over when the board is full"""
        if self.board.is_full():
            self.is_game_over = True
    
    def determine_winner(self):
        """General Mode Rule: player with the most SOS lines wins"""

        red_score = self.SOS_count[self.player_red.color]
        blue_score = self.SOS_count[self.player_blue.color]

        if red_score > blue_score: # if red player has more
            return self.player_red.color
        if blue_score > red_score: # if blue player has more 
            return self.player_blue.color
        
        # if scores are equal 
        return "Draw"