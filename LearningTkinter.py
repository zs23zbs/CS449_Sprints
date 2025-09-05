import tkinter as tk 

window = tk.Tk() 

frame1 = tk.Frame(master=window, width = 200, height = 100, bg = "#40E0D0")
frame1.pack(fill=tk.BOTH, side = tk.LEFT, expand = True)

frame2 = tk.Frame(master=window, width = 50, bg = "#87CEFA")
frame2.pack(fill=tk.BOTH, side = tk.LEFT, expand = True)

frame3 = tk.Frame(master=window, width=25, bg="#BA55D3")
frame3.pack(fill=tk.BOTH, side= tk.LEFT, expand = True)

window.mainloop()