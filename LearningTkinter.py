import tkinter as tk 

window = tk.Tk() # Container for all widgets (text boxes, labels, and buttons)
label = tk.Label( # Only displaying, nothing else
    text="Hello User!",
    foreground = "#6495ED",
    background = "#E6E6FA",
    height = 10,
    width = 20 ).pack()
button = tk.Button(
    text = "Click Here!",
    height = 10,
    width = 20,
    foreground = "#6495ED").pack() # Won't display background color )

window.mainloop() # Event loop for listen for any kind of events 