import tkinter as tk
from game_logic import GameLogic

class SOSGame(): 
    def __init__(self):
        """Creating the start menu for user to interact to initiate game"""

        # Create start_menu instances
        self.start_menu = tk.Tk()
        self.start_menu.title("TicTacToe SOS Start Menu")
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

if __name__ == "__main__":
    SOSGame()