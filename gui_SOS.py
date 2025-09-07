"""This wil be the GUI for the SOS Game"""
import tkinter as tk

window = tk.Tk()
window.title("SOS TicTacToe")

# Create the responsive window
window.rowconfigure(5, minsize= 800, weight = 2)
window.columnconfigure(5, minsize= 800, weight=2)

"""Creating the mode widget"""
mode_frame = tk.Frame(master=window, bd=5, relief=tk.RAISED, width=200, height=100, bg="red")
game_modes = ["Simple Game", "General Game"]
mode_label = tk.Label(master=mode_frame, text="GAME MODE:", fg="pink")

mode_label.grid(row=0, column=0, sticky="ne", padx=3, pady=3)
mode_frame.grid(row=1, column=0)

window.mainloop()