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
        
        # immediately straight to start menu
        self.create_start_menu()
        self.start_menu.mainloop() 

    def create_start_menu(self):
        """Setting up the start menu buttons """

        # Creating the title of the start menu 
        title = tk.Label(self.start_menu, text="SOS Game Setup", font=("Helvetica", 16, "bold"), bg="#008B8B", fg="#FFFAFA")
        title.grid(row=0, column=0, columnspan=3, pady=10)

        # Making the Board Size Spinbox Selection
        board_frame = tk.Frame(self.start_menu, bd=5, relief=tk.RIDGE, bg="#20B2AA",)
        tk.Label(board_frame, text="Board Size:", bg="#FFFAFA", fg="black").grid(row=0, column=0, padx=5, pady=5)
        tk.Spinbox(board_frame, from_=3, to=10, textvariable=self.board_size, width=5).grid(row=0, column=1, padx=5, pady=5)
        board_frame.grid(row=1, column=0, columnspan=2, pady=5)

        # Making the Game Mode Options Button
        mode_frame = tk.Frame(self.start_menu, bd=5, relief=tk.RIDGE, bg="#20B2AA")
        tk.Label(mode_frame, text="Game Mode:", bg="#FFFAFA", fg="black").grid(row=0,column=0, padx=5,pady=5)
        tk.OptionMenu(mode_frame, self.mode, "Simple Game", "General Game").grid(row=0, column=1, padx=5, pady=5)
        mode_frame.grid(row=2, column=0, columnspan=2, pady=5)

    def set_letter_selection (self, player_color, letter):
        pass

    def create_game_widgets(self):
        pass

    def start_game(self):
        pass

    def create_board(self, size):
        pass

    def draw_sos_line(self, lines_info): # will heavily refactor later 
        pass 

    def reset_game(self):
        pass

    def end_game(self):
        pass

if __name__ == "__main__":
    SOSGame()