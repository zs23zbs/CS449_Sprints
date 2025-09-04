import tkinter as tk 

window = tk.Tk() # Container for all widgets (text boxes, labels, and buttons)
label = tk.Label( # Only displaying, nothing else
    text="Hello User! Please enter your name below",
    foreground = "#6495ED",
    background = "black",
    height = 10,
    width = 20 ).pack()
button = tk.Button(
    text = "Click Here!",
    height = 10,
    width = 20,
    foreground = "#6495ED").pack() 
entry = tk.Entry(
    background = "#8FBC8B",
    foreground = "#FFE4C4",
    width = 20 ).pack()
window.mainloop() # Event loop for listen for any kind of events 