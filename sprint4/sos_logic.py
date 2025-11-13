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
        self.current_turn = player_blue 
        self.score_count = {self.player_blue.color : 0, self.player_red.color: 0} # sets the initial score to zero 
    
        self.is_game_over = False
        self.game_mode = ""
    
    @abstractmethod
    def check_game_over(self):
        pass
    
    @abstractmethod
    def determine_winner(self):
        pass
    
    # might need to heavily refactor depending how gui file turns out 
    def making_move(self, row, col, letter): # For human player
        """Human Player make a move on board"""        
        current_player_color = self.current_turn.color # get the which players color turn is it 
        valid_move = self.board.place(row, col, letter, current_player_color) # current player makes a valid move 

        # if current players move make an SOS
        if valid_move:
            found_sos = self.board.check_for_SOS(row, col) #checks if a sos pattern was found 
            score_made = len(found_sos) > 0 # boolean if a score was made 

            # increment current (red or blue) player who scored with an sos pattern 
            if score_made: 
                self.score_count[current_player_color] += len(found_sos)
            
            # if simple mode when player scores then game over
            if self.game_mode == "Simple Game":
                self.is_game_over = True

            # otherwise switch turns in General Game (if sos pattern not made)
            elif self.game_mode == "General Game":
                if not score_made: 
                    self.switch_turn()
            
            self.check_game_over()

            #Incredibily doubt this will work but a placement for now for indicating with sos patterns belong to who  
            gui_line_color = current_player_color.lower()
            human_lines = [(start, end, gui_line_color) for start, end in found_sos]
            return human_lines
        
        return False

    # might need to heavily refactor depending how gui file turns out 
    def computers_move(self):
       """Computer Player make a move on board"""
       
       while (isinstance(self.current_turn, ComputerPlayer) and not self.is_game_over):
        computers_move = self.current_turn.get_move(self.board) # computer gets a valid move
        
        if computers_move: 
            computers_turn = self.current_turn
            computers_color = self.current_turn.color

            row, col, letter = computers_move # unpack computer move entry 
            self.board.place(row, col, letter, computers_color) # place computers move on game board
            made_sos = self.board.check_for_SOS(row, col) # check if computer makes an SOS pattern
            computer_score = len(made_sos) > 0

            if made_sos:
                self.score_count[computers_turn] += len(made_sos)
               
            if self.game_mode == "Simple Game":
                self.is_game_over = True 

            elif self.game_mode == "General Game":
                if not made_sos: 
                    self.switch_turn()
            
            self.check_game_over()

            #Incredibily doubt this will work but a placement for now for indicating with sos patterns belong to who  
            gui_line_color = computers_color.lower()
            computer_lines = [(start, end, gui_line_color) for start, end in computer_score]
            return computer_lines
       
        return False    
                
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
        self.game_mode == "Simple Game"

    def check_game_over(self):
        """Game is over the board is full"""
        if self.board.is_full():
            self.is_game_over = True 

    def determine_winner(self):
        """Simple Mode rule: First player to create an SOS pattern is the winner, otherwise draw"""
        # sets whose score is who
        red_score = self.score_count["Red"]
        blue_score = self.score_count["Blue"]

        if red_score > 0 and blue_score == 0: 
            return self.player_red.color # red is the winner
        elif blue_score > 0 and red_score == 0: 
            return self.player_blue.color # blue is the winner 
        
        # no one scored
        return "Draw"

class GeneralMode(SOSLogic):
    def __init__(self, game_board_size):
        super().__init(game_board_size)
        self.game_mode == "General Game"
    
    def check_game_over(self):
        """Game is over the board is full or players have the same score"""
        if self.score_count["Red"] == self.score_count["Blue"] or self.board.is_full():
            self.is_game_over = True 
    
    def determine_winner(self):
        """General Mode rule: The player with the highest score (most sos patterns) wins, otherwise draw"""
        # sets whose score is who
        red_score = self.score_count["Red"]
        blue_score = self.score_count["Blue"]

        if red_score > blue_score: # if red scores more 
            return self.player_red.color # red wins
        elif blue_score > red_score: # if blue scores more 
            return self.player_blue.color # blue wins
        
        return "Draw" # if niether condition works 