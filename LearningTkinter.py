import tkinter as tk 

window = tk.Tk() # Container for all widgets (text boxes, labels, and buttons)
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack() 
window.mainloop() # Event loop for listen for any kind of events 