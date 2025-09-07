"""Practice/Seeing Versions of a GUI"""
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

#Functions for commands (interactive part)
def open_file():
    """Opens a file to edit"""
    filepath = askopenfilename( # displays a file open dialog and stors the selected file path to "filepath"
        filetypes =[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath: # Checks if the user closes or cancels access to the filepath
        return
    txt_edit.delete("1.0", tk.END) # clears contents 
    with open(filepath, mode="r", encoding="utf-8") as input_file: # Opens selected file and reads contents before storage 
        text = input_file.read()
        txt_edit.insert(tk.END, text) # Assigns string text to txt_edit
    window.title(f"Simple Text Editor - {filepath}") # Sets the title of the window that contains the path to the open file

def save_file():
    """Save the current file as a new file"""
    filepath = asksaveasfilename( # gets the desired save location from the user then stored in "filepath"
        defaultextension = ".txt",
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file: # Creates a new file at selected file path
        text = txt_edit.get("1.0", tk.END) # Takes text from the txt_edit with .get() and assigns to variable "text"
        output_file.write(text) # Writes to output file 
        window.title(f"Simple Text Editor - {filepath}") # Updates the title window

window = tk.Tk()
window.title("Simple Text Editor")

#Creating a responsive window
window.rowconfigure(0, minsize=800, weight=1) 
window.columnconfigure(2, minsize=800, weight=1)

#Creating the four widgets 
txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief = tk.RAISED, bd=10) 
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="Save as...", command=save_file)

#Create the grid for the buttons, with two rows and one column
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

#Create a grid for the window 
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()