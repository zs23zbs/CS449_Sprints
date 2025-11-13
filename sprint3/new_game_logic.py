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

    def make_move(self, row, col, letter):
        """Plase letter that user selected on board and handle the game's current state"""
        current_color = self.current_turn.color # Either Red or Blue

        move_successful = self.board.place(row, col, letter, current_color) # place letter using whichever was selected
        if move_successful:
            lines_coords = self.board.check_for_SOS(row, col)
            score_made = len(lines_coords) > 0

            # update score 
            if score_made:
                self.SOS_count[current_color] += len(lines_coords)

            if self.game_mode_name == "Simple Game":
               self.switch_turn()
           # General Mode: Only switch turn if NO score was made.
            elif self.game_mode_name == "General Game":
               if not score_made:
                   self.switch_turn()
                   
            self.check_game_over()
            gui_line_color = current_color.lower()
            colored_lines_info = [(start, end, gui_line_color) for start, end in lines_coords]
            return colored_lines_info
        return False
    
    def switch_turn(self):
        """Switch turns between the players with each move made"""
        if self.current_turn == self.player_blue:
            self.current_turn = self.player_red
        else: 
            self.current_turn = self.player_blue

    def reset(self):
        """Reset the board whenever called"""
        self.board.reset()
        self.current_turn = self.player_blue
        self.SOS_count = {self.player_red.color : 0, self.player_blue.color : 0}
        self.is_game_over = False
    
class SimpleMode(SOSGameLogic):
    def __init__(self, game_board_size):
        super().__init__(game_board_size)
        self.game_mode_name = "Simple Game"

    def check_game_over(self):
        """Game over if any player scored first or board is full"""
        # game over if score exist or board is completely full
        if self.SOS_count["Red"] > 0 or self.SOS_count["Blue"] > 0 or self.board.is_full():
            self.is_game_over = True
    
    def determine_winner(self):
        """Simple Mode rule: First player to score is the winner, otherwise Draw"""
        red_score = self.SOS_count["Red"]
        blue_score = self.SOS_count["Blue"]

        # check who scored first 
        if red_score > 0 and blue_score == 0: 
            return self.player_red.color
        if blue_score > 0 and red_score == 0:
            return self.player_blue.color
        
        # for when the board is full and no one score a point
        return "Draw"
    
class GeneralMode(SOSGameLogic):
    def __init__(self, game_board_size):
        super().__init__(game_board_size)
        self.game_mode_name = "General Game"

    def check_game_over(self):
        """Game over when board is full"""
        if self.board.is_full():
            self.is_game_over = True 
    
    def determine_winner(self):
        """General Mode rule: player with the highest score wins """
        red_score = self.SOS_count["Red"]
        blue_score = self.SOS_count["Blue"]

        if red_score > blue_score:
            return self.player_red.color
        if blue_score > red_score:
            return self.player_blue.color

        return "Draw"