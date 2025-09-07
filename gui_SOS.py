"""This wil be the GUI Program for the SOS Game"""
import tkinter as tk

window = tk.Tk()
window.title("SOS TicTacToe")

"""Creating TicTacToe Board"""
for i in range(5):
    window.columnconfigure(i, weight=5, minsize=100)
    window.rowconfigure(i, weight=5, minsize=100)

    for j in range(1,6):
        boardGame_frame = tk.Frame(
            master=window,
            relief= tk.SUNKEN,
            bd=5,
        )
        boardGame_frame.grid(row=i, column=j,padx=5, pady=5)
        boardGame_label = tk.Label(master=boardGame_frame, width=8, height=5, text="", bg="lightblue")
        boardGame_label.pack(padx=5, pady=5)

"""Board Size widget"""
boardSize_frame = tk.Frame(master=window, bd=3, relief=tk.RAISED, bg="#008B8B")
boardSize_label = tk.Label(master=boardSize_frame, text=" Board Size: 5", fg="black", bg="#E0FFFF")
boardSize_label.grid(row=0, column=6, sticky="ne", padx=5, pady=5)
boardSize_frame.grid(row=0, column=6, sticky="ne")

"""Creating the mode widget"""
mode_frame = tk.Frame(master=window, bd=1, relief=tk.RAISED, bg="#20B2AA")
mode_label = tk.Label(master=mode_frame, text=f"MODE:", fg="black", bg="#E0FFFF")
game_modes = ["Simple Game", "General Game"]

def pick_mode(): # Fuction for selecting whichever game mode for the radio button
    mode_label.config(text=f"MODE: {variable.get()}")
variable = tk.StringVar(mode_frame, f"{game_modes[0]}")

for i, modes in enumerate(game_modes): # Iterate through the game_modes list to display the different game versions users wants 
    tk.Radiobutton(
        master=mode_frame,
        text=modes,
        variable=variable,
        value=modes,
        command = pick_mode
    ).grid(row=i+1, column=0, sticky="ew", padx=4, pady=4)

mode_label.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
mode_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

window.mainloop()