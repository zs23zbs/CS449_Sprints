import tkinter as tk
from game_logic import GameLogic

class SOSGame(): 
    def __init__(self):
        """Creating the start menu for user to interact to initiate game"""

        # Create start_menu instances
        self.start_menu = tk.Tk()
        self.start_menu.title("SOS Start Menu")
        self.start_menu.config(bg="#008B8B")

        # Variables for start menu
        self.board_size = tk.IntVar(value=3)
        self.mode = tk.StringVar(value="Simple Game")
        self.red_letter = tk.StringVar(value="O")
        self.blue_letter = tk.StringVar(value="S")

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
            tk.Radiobutton(red_frame, text=letter, variable=self.red_letter, value=letter, command=self.update_opponent_letter, bg="#E9967A").grid(row=3, column=0, columnspan=2, pady=5)
        red_frame.grid(row=3, column=0, columnspan=2, pady=5)

        # Start button 
        start_frame = tk.Frame(self.start_menu, bd=5, relief=tk.RAISED, bg="#008B8B")
        tk.Button(start_frame, text="Start Game", height=2, fg="black", bg="#FFFAFA", command=self.start_game).grid(row=0, column=0, padx=10, pady=10)
        start_frame.grid(row=4, column=0, columnspan=2, pady=10)

    def update_opponent_letter(self):
        """Automatically assign the opponent the other label based on user letter choice"""
        self.blue_letter.set("O" if self.red_letter.get() == "S" else "S")

    def start_game(self):
        """Closes the start menu and open the window for game"""
        self.start_menu.destroy()

        self.game_window = tk.Tk()
        self.game_window.title("SOS Game")
        self.game_window.config(bg="#008B8B")

        self.game = GameLogic(self.board_size.get(), self.mode.get())
        self.game.pkayer_red.letter_choice = self.red_letter.get()
        self.game.player_blue.letter_choice = self.blue_letter.get()

        self.board_buttons = []

        # self.create_game_widgets()
        #self.create_board(self.board_size.get())
        #self.update_turn_display()

        self.game_window.mainloop()

if __name__ == "__main__":
    SOSGame()