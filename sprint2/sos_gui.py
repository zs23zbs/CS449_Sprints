import tkinter as tk
from tkinter import messagebox
from game_logic import GameLogic

class SOSGame(): 
    def __init__(self):
        """Creating the start menu for user to interact to initiate game"""

        # Create start_menu instances
        self.start_menu = tk.Tk()
        self.start_menu.title("SOS Start Menu")
        self.start_menu.config(bg="#008B8B")

        # Variables for start menu, must change to accomdate turn mechanics 
        self.board_size = tk.IntVar(value=3)
        self.mode = tk.StringVar(value="Simple Game")
        self.red_letter = tk.StringVar(value="S")
        self.blue_letter = tk.StringVar(value="O")

        self.create_start_menu()
        self.start_menu.mainloop()

    def create_start_menu(self):
        """Setting up the start menu"""

        # Title for Start Menu 
        title = tk.Label(self.start_menu, text="Game Setup", font=("Helvetica", 16, "bold"), bg="#008B8B", fg="#FFFAFA")
        title.grid(row=0, column=0, columnspan=3, pady=10)

        # Board size button 
        board_frame = tk.Frame(self.start_menu, bd=5, relief=tk.RAISED, bg="#20B2AA")
        tk.Label(board_frame, text="Board Size:", bg="#FFFAFA", fg="black").grid(row=0,column=0, padx=5,pady=5)
        tk.Spinbox(board_frame, from_=3, to=10, textvariable=self.board_size, width=5).grid(row=0, column=1, padx=5, pady=5)
        board_frame.grid(row=1, column=0, columnspan=2, pady=5)

        # Game Mode button
        mode_frame = tk.Frame(self.start_menu, bd=5, relief=tk.RAISED, bg="#20B2AA")
        tk.Label(mode_frame, text="Game Mode:", bg="#FFFAFA", fg="black").grid(row=0,column=0, padx=5,pady=5)
        tk.OptionMenu(mode_frame, self.mode, "Simple Game", "General Game").grid(row=0, column=1, padx=5, pady=5)
        mode_frame.grid(row=2, column=0, columnspan=2, pady=5)

        # Red Player button  
        red_frame = tk.Frame(self.start_menu, bd=5, relief=tk.RAISED, bg="#DC143C")
        tk.Label(red_frame, text="Red Player Letter:", bg="#E9967A", fg="black").grid(row=0, column=0, padx=5, pady=5)
        for i, letter in enumerate(["S", "O"]):
            tk.Radiobutton(red_frame, text=letter, variable=self.red_letter, value=letter, command=self.update_opponent_letter, bg="#E9967A").grid(row=0, column=i+1, padx=5, pady=5)
        red_frame.grid(row=3, column=0, columnspan=2, pady=5)

        # Blue Player button
        blue_frame = tk.Frame(self.start_menu, bd=5, relief=tk.RAISED, bg="#0000CD")
        tk.Label(blue_frame, text="Blue Player Letter:",  bg="#1E90FF", fg="black").grid(row=0, column=0, padx=5, pady=5)
        for i, letter in enumerate(["S", "O"]):
            tk.Radiobutton(blue_frame, text=letter, variable=self.blue_letter, value=letter, command=self.update_opponent_letter, bg="#E9967A").grid(row=0, column=i+1, padx=5, pady=5)
        blue_frame.grid(row=4, column=0, columnspan=2, pady=5)

        # Start button 
        start_frame = tk.Frame(self.start_menu, bd=5, relief=tk.RAISED, bg="#008B8B")
        tk.Button(start_frame, text="Start Game", height=2, fg="black", bg="#FFFAFA", command=self.start_game).grid(row=0, column=0, padx=10, pady=10)
        start_frame.grid(row=5, column=0, columnspan=2, pady=10)

    def update_opponent_letter(self):
        """Automatically assign the opponent the other label based on user letter choice"""
        self.blue_letter.set("O" if self.red_letter.get() == "S" else "S")
        self.red_letter.set("S" if self.blue_letter.get() == "O" else "O")

    def start_game(self):
        """Closes the start menu and open the window for game"""
        self.start_menu.destroy()

        self.game_window = tk.Tk()
        self.game_window.title("SOS Game")
        self.game_window.config(bg="#008B8B")

        self.game = GameLogic(self.board_size.get(), self.mode.get())

        self.game.player_red.letter_choice = self.red_letter.get()
        self.game.player_blue.letter_choice = self.blue_letter.get()

        self.board_buttons = []

        self.create_game_widgets()
        self.create_board(self.board_size.get())
        self.update_turn_display()

        self.game_window.mainloop()
    
    def create_game_widgets(self):
        """Layout widgets"""

        # Turn label 
        turn_frame = tk.Frame(self.game_window, bd=5, relief=tk.RAISED, bg="#20B2AA")
        self.turn_label = tk.Label(turn_frame, text="", font=("Helvetica", 16, "bold"), bg="#FFFAFA")
        self.turn_label.pack(padx=5, pady=5)
        turn_frame.pack(pady=10)

        # Mode Label 
        mode_frame = tk.Frame(self.game_window, bd=3, relief=tk.RIDGE, bg="#008B8B")
        self.mode_label = tk.Label(mode_frame, text=f"Game Mode: {self.mode.get()}", font=("Helvetica", 14, "bold"), bg="#E0FFFF",fg="black")
        self.mode_label.pack(padx=5, pady=3)
        mode_frame.pack(pady=5)

        # Player information (Red Player)
        info_frame = tk.Frame(self.game_window, bg="#008B8B")

        red_frame = tk.Frame(info_frame, bd=5, relief=tk.RAISED, bg="#DC143C")
        self.red_label = tk.Label(red_frame, text="", bg="#E9967A", fg="black", font=("Helvetica", 16, "bold"))
        self.red_label.pack(padx=10, pady=5)
        red_frame.grid(row=0, column=0, padx=10)

        # Player information (Blue Player)
        blue_frame = tk.Frame(info_frame, bd=5, relief=tk.RAISED, bg="#0000CD")
        self.blue_label = tk.Label(blue_frame, text="", bg="#1E90FF", fg="black", font=("Helvetica", 16, "bold"))
        self.blue_label.pack(padx=10, pady=5)
        blue_frame.grid(row=0, column=1, padx=10)

        info_frame.pack(pady=10)

        # Place the board game cells 
        self.board_frame = tk.Frame(self.game_window, bg="lightblue", bd=5, relief=tk.RAISED)
        self.board_frame.pack(padx=20, pady=10)

        # Buttons at the bottom (reset, new, and exit game)
        button_frame = tk.Frame(self.game_window, bd=5, relief=tk.RAISED, bg="#008B8B")

        tk.Button(button_frame, text="REPLAY GAME", height=2, bg="#FFFAFA", command=self.reset_game).grid(row=0, column=0, padx=4, pady=4)

        tk.Button(button_frame, text="NEW GAME", height=2, bg="#FFFAFA", command=self.start_game_from_setup).grid(row=0, column=1, padx=4, pady=4)

        tk.Button(button_frame, text="EXIT GAME", height=2, bg="#FFFAFA", command=self.game_window.destroy).grid(row=0, column=2, padx=4, pady=4)

        button_frame.pack(pady=10)
    
    def create_board(self, size):
        """Creating the button grid for the game board"""

        for i in range(size):
            row_buttons = []
            for j in range(size):
                button = tk.Button(
                    master=self.board_frame,
                    text="",
                    width=6,
                    height=3,
                    bg="white",
                    font=("Helvetica", 16, "bold"),
                    command=lambda r=i, c=j: self.handle_click(r,c)
                )
                button.grid(row=i, column=j, padx=3, pady=3)
                row_buttons.append(button)
            self.board_buttons.append(row_buttons)
    
    def handle_click(self, row, col):
        """Handle the moves on the board"""

        if not self.game:
            return 
        
        current_player = self.game.current_turn
        letter = current_player.letter_choice 

        if self.game.make_move(row, col):
            self.board_buttons[row][col].config(text=letter, fg=current_player.color)
            self.update_turn_display()
        else:
            messagebox.showwarning("Invalid Move", "That cell is already occupied.")

    def update_turn_display(self):

        # We need to change this to accomodate the doc type above
        """Update the player labels and the turn labels"""

        current_player = self.game.current_turn
        self.turn_label.config(text=f"Current Turn: {current_player.color.upper()} ({current_player.letter_choice})")
        self.red_label.config(text=f"RED PLAYER (R): {self.game.player_red.letter_choice}")
        self.blue_label.config(text=f"BLUE PLAYER (B): {self.game.player_blue.letter_choice}")

    def reset_game(self):
        """reset the game"""

        if self.game:
            self.game.reset()
        for row in self.board_buttons:
            for button in row:
                button.config(text="", bg="white")
        self.update_turn_display()

    def start_game_from_setup(self):
        """Return to the start menu"""
        self.game_window.destroy()
        SOSGame()

if __name__ == "__main__": 
    SOSGame()