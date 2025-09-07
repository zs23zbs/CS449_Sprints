"""This wil be the GUI for the SOS Game"""
import tkinter as tk

window = tk.Tk()
window.title("SOS TicTacToe")

# Create the responsive window
window.rowconfigure(5, minsize= 800, weight = 2)
window.columnconfigure(5, minsize= 800, weight=2)

"""Creating the mode widget"""
mode_frame = tk.Frame(master=window, bd=5, relief=tk.RAISED, width=200, height=100, bg="white")
game_modes = ["mode","Simple Game", "General Game"]
mode_label = tk.Label(master=mode_frame, text=f"GAME MODE: {game_modes[0]}", fg="pink")

def pick_mode():
    mode_label.config(text=f"Select a Game Mode: {variable.get()}")
variable = tk.StringVar(mode_frame, f"{game_modes[0]}")

for modes in game_modes:
    tk.Radiobutton(
        master=mode_frame,
        text=modes,
        variable=variable,
        value=modes,
        command = pick_mode
    ).grid(row=2, column=0)

mode_label.grid(row=0, column=0, sticky="ne", padx=3, pady=3)
mode_frame.grid(row=1, column=0)

window.mainloop()