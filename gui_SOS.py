"""This wil be the GUI Program for the SOS Game"""
import tkinter as tk

window = tk.Tk()
window.title("SOS TicTacToe")

"""Creating TicTacToe Board Display"""
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
boardSize_frame = tk.Frame(master=window, bd=5, relief=tk.RAISED, bg="#008B8B")
boardSize_label = tk.Label(master=boardSize_frame, text="Game Board Size: 5", fg="black", bg="#E0FFFF")
boardSize_label.grid(row=0, column=6, sticky="ne", padx=5, pady=5)
boardSize_frame.grid(row=0, column=6, sticky="ne", padx=5, pady=5)

"""Creating the mode widget"""
game_modes = ["Simple Game", "General Game"]
mode_frame = tk.Frame(master=window, bd=5, relief=tk.RAISED, bg="#20B2AA")
mode_label = tk.Label(master=mode_frame, text=f"MODE:", fg="black", bg="#E0FFFF")

def pick_mode(): # Fuction for selecting whichever game mode for the radio button
    mode_label.config(text=f"MODE:")
variable1 = tk.StringVar(mode_frame, f"{game_modes[0]}")

for i, modes in enumerate(game_modes): # Iterate through the game_modes list to display the different game versions users wants 
    tk.Radiobutton(
        master=mode_frame,
        text=modes,
        variable=variable1,
        value=modes,
        command = pick_mode
    ).grid(row=i+1, column=0,padx=4, pady=4)

mode_label.grid(row=0, column=0)
mode_frame.grid(row=0, column=0)

"""Red Player Widget"""
redPlayer_modes = ["Human", "Computer"]
redPlayer_frame = tk.Frame(master=window, bd=5, relief=tk.RAISED, bg="#DC143C")
redPlayer_label = tk.Label(master=redPlayer_frame, text=f"RED PLAYER (R):", fg="black", bg="#E9967A")
 
def pick_playerType1():
    redPlayer_label.config(text=f"RED PLAYER (R):")
variable2 = tk.StringVar(redPlayer_frame, f"{redPlayer_modes[0]}")

for i, player in enumerate(redPlayer_modes):
    tk.Radiobutton(
        master=redPlayer_frame,
        text=player,
        variable=variable2,
        value=player,
        command = pick_playerType1
    ).grid(row=i+3, column=0, padx=4, pady=4)

redPlayer_label.grid(row=2, column=0, padx=4, pady=4)
redPlayer_frame.grid(row=2, column=0, padx=4, pady=4)

"""Blue Player Widget"""
bluePlayer_frame = tk.Frame(master=window, bd=5, relief=tk.RAISED, bg="#0000CD")
bluePlayer_label = tk.Label(master=bluePlayer_frame, text=f"BLUE PLAYER (B):", fg="black", bg="#1E90FF")
bluePlayer_modes = ["Human", "Computer"]

def pick_playerType2():
    bluePlayer_label.config(text=f"BLUE PLAYER (B):")
variable3 = tk.StringVar(bluePlayer_frame, f"{bluePlayer_modes[0]}")

for i, player in enumerate(bluePlayer_modes):
    tk.Radiobutton(
        master=bluePlayer_frame,
        text=player,
        variable=variable3,
        value=player,
        command = pick_playerType2
    ).grid(row=i+3, column=6, padx=5, pady=5)

bluePlayer_label.grid(row=2, column=6, padx=5, pady=5)
bluePlayer_frame.grid(row=2, column=6, padx=5, pady=5)

"""S or O Letter Labels"""
S_O_labels = tk.Frame(master=window, bd=5, relief=tk.SUNKEN, bg="#CD5C5C")


"""Which player is playing Labels"""

"""Replay, New Game, Exit Buttons"""

window.mainloop()