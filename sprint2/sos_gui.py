from game_logic import GameLogic # Import GameLogic (backend)
import tkinter as tk 

"""Initiate and create window with title"""
window = tk.Tk()
window.title("SOS TicTacToe")

"""Variables for Game"""
game = None
board_buttons = []
board_size = tk.IntVar(value=3)
mode = tk.StringVar(value="Simple Game")

def start_game():
    global game, board_buttons

    for row in board_buttons:
        for button in row:
            button.destroy()
    board_buttons = [] 

    size = board_size.get()
    current_mode = mode.get()

"""Board Size widget""" 
boardSize_frame = tk.Frame(master=window, bd=5, relief=tk.RAISED, bg="#008B8B") 
boardSize_label = tk.Label(master=boardSize_frame, text="Game Board Size: ", fg="black", bg="#E0FFFF")

# Format the board size widget 
boardSize_label.grid(row=0, column=6, padx=5, pady=5)
boardSize_frame.grid(row=0, column=6, padx=5, pady=5)

"""Creating the mode widget"""
game_modes = ["Simple Game", "General Game"] # List of options for user to pick for game mode / creating a radio button
mode_frame = tk.Frame(master=window, bd=5, relief=tk.RAISED, bg="#20B2AA")
mode_label = tk.Label(master=mode_frame, text=f"MODE:", fg="black", bg="#E0FFFF")

def pick_mode(): # Fuction for selecting whichever game mode for the radio button
    mode_label.config(text=f"MODE:")
variable1 = tk.StringVar(mode_frame, f"{game_modes[0]}")

for i, modes in enumerate(game_modes): # Iterate through the game_modes list to display the different game versions the user may want to play in 
    tk.Radiobutton(
        master=mode_frame,
        text=modes,
        variable=variable1,
        value=modes,
        command = pick_mode
    ).grid(row=i+1, column=0,padx=4, pady=4)

mode_label.grid(row=0, column=0)
mode_frame.grid(row=0, column=0)

"""Red Player Widget"""
redPlayer_modes = ["Human", "Computer"]
redPlayer_frame = tk.Frame(master=window, bd=5, relief=tk.RAISED, bg="#DC143C")
redPlayer_label = tk.Label(master=redPlayer_frame, text=f"RED PLAYER (R):", fg="black", bg="#E9967A")
 
def pick_playerType1():
    redPlayer_label.config(text=f"RED PLAYER (R):")
variable2 = tk.StringVar(redPlayer_frame, f"{redPlayer_modes[0]}")

for i, player in enumerate(redPlayer_modes): # Loop/iterate through all items in list 
    tk.Radiobutton(
        master=redPlayer_frame,
        text=player,
        variable=variable2,
        value=player,
        command = pick_playerType1
    ).grid(row=i+3, column=0, padx=4, pady=4)

redPlayer_label.grid(row=2, column=0, padx=4, pady=4)
redPlayer_frame.grid(row=2, column=0, padx=4, pady=4)

"""Blue Player Widget"""
bluePlayer_modes = ["Human", "Computer"]
bluePlayer_frame = tk.Frame(master=window, bd=5, relief=tk.RAISED, bg="#0000CD")
bluePlayer_label = tk.Label(master=bluePlayer_frame, text=f"BLUE PLAYER (B):", fg="black", bg="#1E90FF")

def pick_playerType2():
    bluePlayer_label.config(text=f"BLUE PLAYER (B):")
variable3 = tk.StringVar(bluePlayer_frame, f"{bluePlayer_modes[0]}")

for i, player in enumerate(bluePlayer_modes):
    tk.Radiobutton(
        master=bluePlayer_frame,
        text=player,
        variable=variable3,
        value=player,
        command = pick_playerType2
    ).grid(row=i+3, column=6, padx=5, pady=5)

bluePlayer_label.grid(row=2, column=6, padx=5, pady=5)
bluePlayer_frame.grid(row=2, column=6, padx=5, pady=5)

"""Sample SOS line"""
sample_canvas = tk.Canvas(master=window, width=350, height=100) # Create the drawing canvas for strike through line 
sample_canvas.grid(row=3, column=2, columnspan=3, pady=20)

# Draw sample "S O S" lettering
sample_canvas.create_text(60, 50, text="S",fill="black")
sample_canvas.create_text(170, 50, text="O",fill="black")
sample_canvas.create_text(300, 50, text="S",fill="black")

"""Replay, New Game, Exit Buttons"""
#Replay Button Widget 
replay_frame = tk.Frame(master=window, bd =5, relief =tk.RAISED, bg="#008B8B") 
replay_button = tk.Button(master=replay_frame, text="REPLAY GAME", height=2, fg="black", bg="#E0FFFF")
replay_frame.grid(row=6, column=1, padx=4, pady=4)
replay_button.grid(row=6, column=1, padx=4, pady=4)

# New Game Button Widget 
newGame_frame = tk.Frame(master=window, bd=5, relief =tk.RAISED, bg="#008B8B")

newGame_button = tk.Button(
    master=newGame_frame,
    text="NEW GAME",
    height=2,
    fg="black",
    bg="#E0FFFF",
    command=lambda: start_game())

newGame_frame.grid(row=6, column=3, padx=4, pady=4)
newGame_button.grid(row=6, column=3, padx=4, pady=4)

# Exit Button Widget
exit_frame = tk.Frame(master=window, bd=5, relief =tk.RAISED, bg="#008B8B")
exit_button = tk.Button(master=exit_frame, text="EXIT", height=2, fg="black", bg="#E0FFFF")
exit_frame.grid(row=6, column=5, padx=4, pady=4)
exit_button.grid(row=6, column=5, padx=4, pady=4)

"""Record Score Check Box Widget"""
recordScoreVar=bool() # To set the state of the checkbox button, check (TRUE) or uncheck (FALSE)
recordScore_frame = tk.Frame(master=window, bd=5, relief =tk.RAISED, bg="#008B8B")
recordScore_CheckbButton = tk.Checkbutton(master=window, text="RECORD SCORE: ", height=1, fg="black", bg="#E0FFFF")
recordScore_frame.grid(row=4, column=6, padx=4, pady=4)
recordScore_CheckbButton.grid(row=4, column=6, padx=4, pady=4)

window.mainloop()