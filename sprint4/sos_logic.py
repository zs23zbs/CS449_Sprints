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
        self.current_turn = player_blue # reconsider 
        self.score_count = {self.player_blue.color : 0, self.player_red.color: 0} # sets the score to zero 
    
        self.is_game_over = False
        self.game_mode = ""
    
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
        
            # Preare the human players lines (track who scored which pattern)
            gui_lines_color = current_color.lower()
            human_lines_info = [(start, end, gui_lines_color) for start, end in lines_coords]

            computer_lines_info = self.handles_comp_turns() # calling new method 

            human_lines_info.extend(computer_lines_info)
            return human_lines_info
        
        return False

    def handles_comp_turns(self):
        # collect the computers scoring lines 
        total_computer_lines = []

        # makes sure that current turn is the computer players and the game isn't over yet 
        while (isinstance(self.current_turn, ComputerPlayer) and not self.is_game_over): 
            pass