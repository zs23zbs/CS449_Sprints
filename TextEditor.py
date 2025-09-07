import tkinter as tk

window = tk.Tk()
window.title("Simple Text Editor")

#Creating a responsive window
window.rowconfigure(0, minsize=800, weight=1) 
window.columnconfigure(2, minsize=800, weight=1)

#Creating the four widgets 
txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief = tk.RAISED, bd=2)  
btn_open = tk.Button(frm_buttons, text="Open")
btn_save = tk.Button(frm_buttons, text="Save as...")

#Create the grid for the buttons, with two rows and one column
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

#Create a grid for the window 
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()