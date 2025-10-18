from BoardClass import Board
from PlayerClass import Player

# Game Logic Class
# Control the flow of the game 
    # Managing Turns 
    # Move controls 

class GameLogic:
    def __init__(self, game_board_size, mode):
        self.board = Board(game_board_size)
        self.mode = mode

        # Created Objects
        self.player_blue = Player("Blue", "S")
        self.player_red = Player("Red", "S")

        # Start with Blue player's turn 
        self.current_turn = self.player_blue

    def make_move(self, row, col): # Very unsure about method 
        if self.board.is_cell_empty(row, col):
            self.board_game.place(row, col, self.current_turn.letter_choice, self.current_turn.color)
            self.switch_turn()
            return True 
        else: #Move is invalid if the cell is occupied 
            return False
        
    def switch_turn(self): # Switch the current player turn to the opposing player
        if self.current_turn == self.player_blue: 
            self.current_turn = self.player_red
        else:
            self.current_turn = self.player_blue

    def reset(self):
        self.board.reset()
        self.current_turn = self.player_blue