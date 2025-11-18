from board_class import Board
from abc import ABC, abstractmethod  

class SOSLogic(ABC):
    def __init__(self, game_board_size, player_blue, player_red):
        """Initialize instance for logic of game"""
        self.board = Board(game_board_size)
        self.player_blue = player_blue 
        self.player_red = player_red
        self.current_turn = player_blue 
        self.score_count = {self.player_blue.color : 0, self.player_red.color : 0} # sets the initial score to zero 
    
        self.is_game_over = False
        self.game_mode = ""

        self.blue_lines = []
        self.red_lines = []
    
    @abstractmethod
    def check_game_over(self):
        pass
    
    @abstractmethod
    def determine_winner(self):
        pass
     
    def making_move(self, row, col, letter): # For human player
        """Human Player make a move on board"""  

        # set the right variables for the current player + color 
        current_player = self.current_turn      
        current_player_color = current_player.color 

        if not self.board.is_cell_empty(row, col):
            return False, []
        
        valid_move = self.board.place(row, col, letter, current_player_color) 

        if valid_move:
            found_sos = self.board.check_for_SOS(row, col)  
            score_made = len(found_sos) > 0 

            # increment current (red or blue) player scored  
            if score_made: 
                self.score_count[current_player_color] += len(found_sos)

                # adds each players own respective found sos lines to their own list
                if current_player_color == "Blue":
                    self.blue_lines.extend(found_sos)
                else: 
                    self.red_lines.extend(found_sos)
            
            # if simple mode when player makes a score, then game over
            if self.game_mode == "Simple Game":
                if score_made:
                    self.is_game_over = True
                else:
                    self.switch_turn()

            # otherwise switch turns between players in General Game (if sos pattern not made)
            elif self.game_mode == "General Game":
                if not score_made: 
                    self.switch_turn()
            
            self.check_game_over()

            return True, found_sos 
        
        return False, []   
                
    def switch_turn(self):
        """Switch turns between players after each move"""
        if self.current_turn == self.player_blue: 
            self.current_turn = self.player_red
        else: 
            self.current_turn = self.player_blue

    def reset(self):
        """Resets the game board"""
        self.board.reset() 
        self.current_turn = self.player_blue  
        self.score_count = {self.player_blue.color : 0, self.player_red.color: 0} 
        self.is_game_over = False
        self.blue_lines = []
        self.red_lines = []

class SimpleMode(SOSLogic):
    def __init__(self, game_board_size, player_blue, player_red):
        super().__init__(game_board_size, player_blue, player_red)
        self.game_mode = "Simple Game"

    def check_game_over(self):
        """Game is over the board is full"""
        if self.board.is_full():
            self.is_game_over = True 

    def determine_winner(self):
        """Simple Mode rule: First player to create an SOS pattern is the winner, otherwise draw"""
        red_score = self.score_count["Red"]
        blue_score = self.score_count["Blue"]

        if red_score > 0 and blue_score == 0: 
            return "Red" # red is the winner
        elif blue_score > 0 and red_score == 0: 
            return "Blue" # blue is the winner 
        
        return "Draw"

class GeneralMode(SOSLogic):
    def __init__(self, game_board_size, player_blue, player_red):
        super().__init__(game_board_size, player_blue, player_red)
        self.game_mode = "General Game"
    
    def check_game_over(self):
        """Game is over the board is full or players have the same score"""
        if self.board.is_full():
            self.is_game_over = True 
    
    def determine_winner(self):
        """General Mode rule: The player with the highest score (most sos patterns) wins, otherwise draw"""
        red_score = self.score_count["Red"]
        blue_score = self.score_count["Blue"]

        if red_score > blue_score: 
            return "Red" 
        elif blue_score > red_score: 
            return "Blue" 
        
        return "Draw" 