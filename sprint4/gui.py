import tkinter as tk
from sos_logic import SimpleMode, GeneralMode

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

        # Making the Start Game Button
        start_frame = tk.Frame(self.start_menu, bd=5, relief=tk.RIDGE, bg="#008B8B")
        tk.Button(start_frame, text="Start SOS Game", height=2, bg="#FFFAFA", fg="black", command=self.start_game).grid(row=0, column=0, padx=5, pady=5)
        start_frame.grid(row=5, column=0, columnspan=2, pady=10)
    
    def start_game(self):
        """Starting the game window after players enter settings for SOS Game"""

        self.start_menu.destroy() # close the SOS setup menu 

        # Create the game window after set up menu 
        self.game_window = tk.Tk()
        self.game_window.title("SOS Game Window")
        self.game_window.config(bg="#008B8B")

        # Get the board size players selected from spinbox
        board_size = self.board_size.get() 

        # Get the players 
        red_player = self.red_letter_choice.get()
        blue_player = self.blue_letter_choice.get()

        # Determine the Game mode depending on what players have chosen 
        game_mode = self.mode.get()

        if game_mode == "Simple Game":
            self.game = SimpleMode(board_size, blue_player, red_player)
        else:
            self.game = GeneralMode(board_size, blue_player, red_player)

        # set the the game board and widgets 
        self.board_buttons = []
        self.create_game_widgets()
        self.create_board(board_size)

        # update the letter selection 
        self.set_letter_selection("Red", self.red_letter_choice.get())
        self.set_letter_selection("Blue", self.blue_letter_choice.get())
        self.update_turn_display()

        self.game_window.mainloop()
        
    def set_letter_selection (self, player_color, letter):
        """Sets the letters to players with toggle"""

        # Set the S and O letters to the right players 
        if player_color == "Red":
            self.red_letter_choice.set(letter)
            s_btn = self.red_s_button
            o_btn = self.red_o_button
            display_labels = self.red_selection_label
        else:
            self.blue_letter_choice.set(letter)
            s_btn = self.blue_s_button
            o_btn = self.blue_o_button
            display_labels = self.blue_selection_label

        # Highlight the selected letters to show which one is picked 
        if letter == "S":
            s_btn.config(bg="#0C530C", relief=tk.RAISED)
            o_btn.conifg(bg="SystemButtonFace", relief=tk.SUNKEN)
        else:
            s_btn.config(bg="SystemButtonFace", relief=tk.SUNKEN)
            o_btn.config(bg="#0C530C", relief=tk.RAISED)

        # Visually display the selected letter
        if display_labels:
            display_labels.config(text=f"Selected Letter: {letter}", font=("Helvetica", 12, "bold"))

    def create_game_widgets(self):
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