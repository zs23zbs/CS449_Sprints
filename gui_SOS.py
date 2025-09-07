"""This wil be the GUI for the SOS Game"""
import tkinter as tk

window = tk.Tk()
window.title("SOS TicTacToe")

"""Create the responsive window"""
window.rowconfigure(5, minsize= 800, weight = 2)
window.columnconfigure(5, minsize= 800, weight=2)

"""Board Size"""
boardSize_frame = tk.Frame(master=window, bd=3, relief=tk.RAISED, width=800, height=800, bg="red")
boardSize_label = tk.Label(master=boardSize_frame, text=" Board Size: 5", fg="black", bg="blue")
boardSize_label.grid(row=0, column=5, sticky="ne", padx=5, pady=5)
boardSize_frame.grid(row=0, column=5, sticky="ne")

"""Creating the mode widget"""
mode_frame = tk.Frame(master=window, bd=5, relief=tk.RAISED, width=800, height=800, bg="purple")
mode_label = tk.Label(master=mode_frame, text=f"MODE:", fg="black", bg="pink")
game_modes = ["Simple Game", "General Game"]

def pick_mode():
    mode_label.config(text=f"Select a Mode: {variable.get()}")
variable = tk.StringVar(mode_frame, f"{game_modes[0]}")

for i, modes in enumerate(game_modes):
    tk.Radiobutton(
        master=mode_frame,
        text=modes,
        variable=variable,
        value=modes,
        command = pick_mode
    ).grid(row=i+1, column=0, sticky="ew", padx=3, pady=3)

mode_label.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
mode_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

window.mainloop()