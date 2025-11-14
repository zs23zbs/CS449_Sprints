import tkinter as tk

class SOSGame():
    def __init__(self):
        """Initilize instances/vairables for SOS game"""

        # Create start_menu instances 
        self.start_menu = tk.Tk()
        self.start_menu.title("SOS Start Menu")
        self.start_menu.config(bg="#008B8B")

        # Varaibles for start_menu buttons (board size and mode)
        self.board_size = tk.IntVar(value=3) # default/smallest board size
        self.mode = tk.StringVar(value="Simple Game") # default game mode

        # To start with for letter choices
        self.red_letter_choice = tk.StringVar(value="S")
        self.blue_letter_choice = tk.StringVar(value="O")
        self.red_selection_label = None
        self.blue_selection_label = None
        
        self.create_start_menu()
        self.start_menu.mainloop() # immediately straight to start menu

    def start_game(self):
        pass

    def create_start_menu(self):
        pass

    def set_letter_selection (self, player_color, letter):
        pass

    def create_game_widgets(self):
        pass

    def create_board(self, size):
        pass

    def reset_game(self):
        pass

    def end_game(self):
        pass

if __name__ == "__main__":
    SOSGame()