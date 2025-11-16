import tkinter as tk
from sos_logic import SimpleMode, GeneralMode
from player_class import HumanPlayer, ComputerPlayer
from tkinter import messagebox

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
            o_btn.config(bg="SystemButtonFace", relief=tk.SUNKEN)
        else:
            s_btn.config(bg="SystemButtonFace", relief=tk.SUNKEN)
            o_btn.config(bg="#0C530C", relief=tk.RAISED)

        # Visually display the selected letter
        if display_labels:
            display_labels.config(text=f"Selected Letter: {letter}", font=("Helvetica", 12, "bold"))

    def create_game_widgets(self):
        """Creates the game widgets in game window"""

        # Turn Label
        turn_frame = tk.Frame(self.game_window, bd=5, relief=tk.RAISED, bg="#20B2AA")
        self.turn_label = tk.Label(turn_frame, text="....", font=("Helvetica", 16, "bold"), bg="#FFFAFA")
        self.turn_label.pack(padx=5, pady=5)
        turn_frame.pack(pady=10)

        # Game Mode Label 
        mode_frame  = tk.Frame(self.game_window, bd=3, relief=tk.RIDGE, bg="#008B8B")
        self.mode_label = tk.Label(mode_frame, text=f"Game Mode: {self.mode.get()}", font=("Helvetica", 14, "bold"), bg="#E0FFFF", fg="black")
        self.mode_label.pack(padx=5, pady=3)
        mode_frame.pack(pady=5)

        # Creating the frame for the game area
        main_game_area_frame = tk.Frame(self.game_window, bg="#008B8B")
        main_game_area_frame.pack(pady=10)

        # Red player Info
        red_controls_frame = tk.Frame(main_game_area_frame, bg="#008B8B")
        red_controls_frame.grid(row=0, column=0, padx=20, pady=10, sticky=tk.N)

        red_frame = tk.Frame(red_controls_frame, bd=5, relief=tk.RIDGE, bg="red")
        self.red_label = tk.Label(red_frame, text="", bg="#E9967A", fg="black", font=("Helvetica", 14, "bold"))
        self.red_label.pack(padx=10, pady=5)
        red_frame.pack(pady=10)

        red_letter_frame = tk.Frame(red_controls_frame, bd=5, relief=tk.RIDGE, bg="#20B2AA")
        tk.Label(red_letter_frame, text="Selected Move:", bg="#FFFAFA", fg="black").pack(side=tk.TOP, padx=5, pady=5)

        # Red Player toggle buttons for S or O 
        self.red_s_button = tk.Button(red_letter_frame, text="S", width=4, command=lambda: self.set_letter_selection("Red", "S"))
        self.red_o_button = tk.Button(red_letter_frame, text="O", width=4, command=lambda: self.set_letter_selection("Red", "O"))

        self.red_s_button.pack(side=tk.LEFT, padx=5)
        self.red_o_button.pack(side=tk.LEFT, padx=5)
        red_letter_frame.pack(pady=10)

        # red players selection label 
        self.red_selection_label = tk.Label(red_controls_frame, text="", bg="#008B8B", fg="#FFFAFA")
        self.red_selection_label.pack(pady=5)

        # Creating the game board itself
        self.board_container = tk.Frame(main_game_area_frame, bg="lightblue", bd=5, relief=tk.RIDGE)
        self.board_container.grid(row=0, column=1, padx=20, pady=10)

        # Configure the size of game board  
        size = (self.board_size.get()) * 75
        
        self.canvas = tk.Canvas(self.board_container, width=size, bg="white", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Blue player Info
        blue_controls_frame = tk.Frame(main_game_area_frame, bg="#008B8B")
        blue_controls_frame.grid(row=0, column=2, padx=20, pady=10, sticky=tk.N)

        blue_frame = tk.Frame(blue_controls_frame, bd=5, relief=tk.RIDGE, bg="#0000CD")
        self.blue_label = tk.Label(blue_frame, text="", bg="#1E90FF", fg="black", font=("Helvetica", 14, "bold"))
        self.blue_label.pack(padx=10, pady=5)
        blue_frame.pack(pady=10)

        blue_letter_frame = tk.Frame(blue_controls_frame, bd=5, relief=tk.RIDGE, bg="#20B2AA")
        tk.Label(blue_letter_frame, text="Selected Move:", bg="#FFFAFA", fg="black").pack(side=tk.TOP, padx=5, pady=5)

        # Blue player toggle button for S or O
        self.blue_s_button = tk.Button(blue_letter_frame, text="S", width=4, command=lambda: self.set_letter_selection("Blue", "S"))
        self.blue_o_button = tk.Button(blue_letter_frame, text="O", width=4, command=lambda: self.set_letter_selection("Blue", "O"))
        
        self.blue_s_button.pack(side=tk.LEFT, padx=5)
        self.blue_o_button.pack(side=tk.LEFT, padx=5)
        blue_letter_frame.pack(pady=10)

        # blue players selection label
        self.blue_selection_label = tk.Label(blue_controls_frame, text="", bg="#008B8B", fg="#FFFAFA")
        self.blue_selection_label.pack(pady=5)

        # Bottom Game widget buttons 
        button_bottom_frame = tk.Frame(self.game_window, bd=5, relief=tk.RIDGE, bg="#008B8B")

        tk.Button(button_bottom_frame, text="REPLAY GAME", height=2, bg="#FFFAFA", command=self.reset_game).grid(row=0, column=0, padx=4, pady=4)
        tk.Button(button_bottom_frame, text="NEW GAME", height=2, bg="#FFFAFA", command=self.start_game_from_setup).grid(row=0, column=1, padx=4, pady=4)
        tk.Button(button_bottom_frame, text="EXIT GAME", height=2, bg="#FFFAFA", command=self.game_window.destroy).grid(row=0, column=2, padx=4, pady=4)
        button_bottom_frame.pack(pady=10)

    def create_board(self, size):
        """Making the button grid for the actual game board"""

        # Set up the board game variables
        self.board_buttons = []
        self.canvas.delete("all")
        self.canvas.update_idletasks()
        cell_width = self.canvas.winfo_width() / size
        cell_height = self.canvas.winfo_height() / size

        # Create the board, and make the cells clickable 
        for i in range(size):
            row_buttons = []
            for j in range(size):
                button = tk.Button(
                    master=self.canvas,
                    text="",
                    width=6, 
                    height=3,
                    bg="white",
                    font=("Helvetica", 16, "bold"),
                    command=lambda r=i,  c=j: self.handle_clicks(r,c))
                
                x_center = j * cell_width + cell_width / 2
                y_center = i * cell_height + cell_height / 2
                self.canvas.create_window(x_center, y_center, window=button, anchor=tk.CENTER)
                row_buttons.append(button)
                self.board_buttons.append(row_buttons)

    """New/Major Changes for class methods (I probably need) to accommodate for Human and Computer Components"""
    def handle_clicks(self, row, col):
        """Handles the clicks or events for Human Player on the game board"""

        # Display a message for when the game is over 
        if self.game.is_game_over:
            messagebox.showinfo("GAME OVER!", "The SOS Game has ended. Please select NEW GAME, REPLAY GAME, or EXIT GAME")
            return None
        
        current_player_before_move = self.game.current_turn

        # Current players clicks go through ONLY if current player is the human player 
        if not isinstance(current_player_before_move, HumanPlayer):
            return None 
        
        # Set the color letter to whoever is the current player during turn 
        if current_player_before_move == "Red":
            letter = self.red_letter_choice.get()
        else: 
            letter = self.blue_letter_choice.get()

        success, found_sos = self.game.making_move(row, col, letter)

        # if the move was successful, visually update the game state
        if success: 
            self.process_visual_updates(row, col, letter, current_player_before_move.color, found_sos)

            if not self.game.is_game_over:
                self.update_turn_display()
                self.update_player_controls()

                current_player_before_move = self.game.current_turn

                # start the computers move sequence with a slight delay 
                if isinstance(current_player_before_move, ComputerPlayer):
                    self.game_window.after(60, self.computer_move_sequence)
        else: 
            messagebox.showerror("Invalid Move!", "Selected CELL is occupied!")

    def update_turn_display(self):
        pass

    def update_player_controls(self):
        pass

    def process_visual_updates(self, row, col, letter, color, found_sos):
        pass

    def draw_sos_line(self):
        pass

    def computer_move_sequence(self):
        pass

    def reset_game(self):
        """Reset the game"""

        if self.game:
            self.game.reset()
        for row in self.board_buttons:
            for button in row: 
                button.config(text="", fg="black", bg="white")

        self.set_letter_selection("Red", "S")
        self.set_letter_selection("Blue", "S")
        self.update_turn_display()

    def end_game(self):
        """Determine the winner of the game"""
        winner = self.game.determine_winner()

        self.update_turn_display()

        if winner == "Draw":
            self.turn_label.config(text="GAME OVER: IT'S A DRAW!")
            messagebox.showinfo("Game Over", f"The {self.mode.get()} has ended in a Draw!")
        else:
            self.turn_label.config(text=f"GAME OVER: {winner.upper()} WINS!")
            messagebox.showinfo("Game Over", f"The {self.mode.get()} Winner is: {winner.upper()}!")
            
    def start_game_from_setup(self):
        self.game_window.destroy()
        SOSGame()

if __name__ == "__main__":
    SOSGame()