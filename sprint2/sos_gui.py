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

        title = tk.Label(self.start_menu, text="Game Setup", font=("Helvetica", 16, "bold"), bg="#008B8B", fg="#FFFAFA")
        title.grid(row=0, column=0, columnspan=3, pady=10)

if __name__ == "__main__":
    SOSGame()