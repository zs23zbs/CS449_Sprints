import tkinter as tk
from game_logic import GameLogic

class SOSGame(): 
    def __init__(self):
        """Creating the start menu for user to interact to initiate game"""
        self.start_menu = tk.Tk()
        self.start_menu.title("TicTacToe SOS Start Menu")
        self.start_menu.config(bg="#008B8B")


if __name__ == "__main__":
    SOSGame()