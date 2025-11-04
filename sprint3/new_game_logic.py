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
            score_gained = self.board.check_for_SOS(row, col)
            score_made = score_gained > 0

            if score_made: # add integer count to score
                self.SOS_count[current_color] += score_gained

            if self.game_mode_name == "Simple Game":
                # Simple mode, swtich turns, game ends with whoever scores first
                self.switch_turn()
            elif self.game_mode_name == "General Game":
                # General mode, swithc turns only if no score was made
                if not score_made:
                    self.switch_turn()
            self.check_game_over() # for checking game over

            return True
        return False
    
    def switch_turn(self):
        """Switch turns between the players with each move made"""
        if self.current_turn == self.player_blue:
            self.current_turn = self.player_red
        else: 
            self.current_turn = self.player_blue

    def reset(self):
        self.board.reset
        self.current_turn = self.player_blue
        self.SOS_count = {self.player_red.color : 0, self.player_blue.color : 0}
        self.is_game_over = False