import tkinter as tk

def decrease():
    value = int(lb1_value["text"])
    lb1_value["text"] =f"{value -1}"

def increase():
   value = int(lb1_value["text"])
   lb1_value["text"] =f"{value +1}"

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0,1,2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

# Retrieve a label's text
label = tk.Label(text="Hello")
text = label["text"]

# set new text for the label 
label["text"] = "Good bye"

lb1_value = tk.Label(master=window, text="0")
lb1_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()