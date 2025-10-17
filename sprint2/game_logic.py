from BoardClass import Board
from PlayerClass import Player

# Game Logic Class
# Control the flow of the game 
    # Managing Turns 
    # Move controls 

class GameLogic:
    def __init__(self, board, mode):
        self.board = board
        self.mode = mode

        # Created Objects
        self.player_blue = Player("Blue", "S")
        self.player_red = Player("Red", "S")

        # Start with Blue player's turn 
        self.current_turn = self.player_blue

    def make_move(self, row, col): # Very unsure about method 
        if self.board_game.is_cell_empty(row, col) == True:
            self.current_turn = self.letter, self.color # set to current player 
            self.board_game.place(row, col, self.letter, self.color) # place a move on a cell
            self.current_turn = "Red" # change the player color to indicate "switching to other player"
        else:
            return False
        
    def switch_turn():
        pass