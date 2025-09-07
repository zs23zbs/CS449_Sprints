import tkinter as tk

window = tk.Tk()
window.title("Simple Text Editor")

#Creating a responsive window
window.rowconfigure(0, minsize=800, weight=1) 
window.columnconfigure(2, minsize=800, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief = tk.RAISED, bd=2)  #
btn_open = tk.Button(frm_buttons, text="Open")
btn_save = tk.Button(frm_buttons, text="Save as...")