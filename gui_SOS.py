"""This wil be the GUI Program for the SOS Game"""
import tkinter as tk

window = tk.Tk()
window.title("SOS TicTacToe")

"""Create the responsive window"""
window.rowconfigure(5, minsize= 800, weight = 2)
window.columnconfigure(5, minsize= 800, weight=2)

"""TicTacToe Board widget"""
class TicTacToeBoard(tk.Tk()):
    def __init__(self):
        super().__init__()
        self._cells= {}
    
    def game_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master= display_frame,
            text="Ready?",
            font = font.Font(size=10, weight="bold")
        )
        self.display.pack()

"""Board Size widget"""
boardSize_frame = tk.Frame(master=window, bd=3, relief=tk.RAISED, bg="#008B8B")
boardSize_label = tk.Label(master=boardSize_frame, text=" Board Size: 5", fg="black", bg="#E0FFFF")
boardSize_label.grid(row=0, column=5, sticky="ne", padx=5, pady=5)
boardSize_frame.grid(row=0, column=5, sticky="ne")

"""Creating the mode widget"""
mode_frame = tk.Frame(master=window, bd=5, relief=tk.RAISED, bg="#20B2AA")
mode_label = tk.Label(master=mode_frame, text=f"MODE:", fg="black", bg="#E0FFFF")
game_modes = ["Simple Game", "General Game"]

def pick_mode(): # Fuction for selecting whichever game mode for the radio button
    mode_label.config(text=f"MODE: {variable.get()}")
variable = tk.StringVar(mode_frame, f"{game_modes[0]}")

for i, modes in enumerate(game_modes): # Iterate through the game_modes list to display the different versions users wants 
    tk.Radiobutton(
        master=mode_frame,
        text=modes,
        variable=variable,
        value=modes,
        command = pick_mode
    ).grid(row=i+1, column=0, sticky="ew", padx=6, pady=6)

mode_label.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
mode_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)


window.mainloop()