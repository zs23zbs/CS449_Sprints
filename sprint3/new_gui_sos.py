from new_player_class import Player           
from new_game_logic import SimpleMode, GeneralMode
import tkinter as tk
from tkinter import messagebox

class SOSGame():
    def __init__(self):
        # create the start_menu instances
        self.start_menu = tk.Tk()
        self.start_menu.title("SOS Start Menu")
        self.start_menu.config(bg="#008B8B")

        # variables for start_menu
        self.board_size = tk.IntVar(value=3)
        self.mode = tk.StringVar(value="Simple Game")
        
        self.red_letter_choice = tk.StringVar(value="S")
        self.blue_letter_choice = tk.StringVar(value="S")


        self.red_selection_label = None
        self.blue_selection_label = None


        self.create_start_menu()
        self.start_menu.mainloop()
    
    def create_start_menu(self):
        """Setting up the start menu"""

        # Title for the starting menu
        title = tk.Label(self.start_menu, text="Game Setup", font=("Helvetica", 16, "bold"), bg="#008B8B", fg="#FFFAFA")
        title.grid(row=0, column=0, columnspan=3, pady=10)

        # Board size button
        board_frame = tk.Frame(self.start_menu, bd=5, relief=tk.RAISED, bg="#20B2AA")
        tk.Label(board_frame, text="Board Size:", bg="#FFFAFA", fg="black").grid(row=0,column=0, padx=5,pady=5)
        tk.Spinbox(board_frame, from_=3, to=10, textvariable=self.board_size, width=5).grid(row=0, column=1, padx=5, pady=5)
        board_frame.grid(row=1, column=0, columnspan=2, pady=5)

        # Selecting the game mode button
        mode_frame = tk.Frame(self.start_menu, bd=5, relief=tk.RAISED, bg="#20B2AA")
        tk.Label(mode_frame, text="Game Mode:", bg="#FFFAFA", fg="black").grid(row=0,column=0, padx=5,pady=5)
        tk.OptionMenu(mode_frame, self.mode, "Simple Game", "General Game").grid(row=0, column=1, padx=5, pady=5)
        mode_frame.grid(row=2, column=0, columnspan=2, pady=5)

        # Start game button
        start_frame = tk.Frame(self.start_menu, bd=5, relief=tk.RAISED, bg="#008B8B")
        tk.Button(start_frame, text="Start Game", height=2, fg="black", bg="#FFFAFA", command=self.start_game).grid(row=0, column=0, padx=10, pady=10)
        start_frame.grid(row=5, column=0, columnspan=2, pady=10)
    
    def start_game(self):
        self.start_menu.destroy()

        self.game_window = tk.Tk()
        self.game_window.title("SOS Game")
        self.game_window.config(bg="#008B8B")

        # Creating the game board based on size selected
        board_size = self.board_size.get()
        game_mode = self.mode.get()
        if game_mode == "Simple Game":
            self.game = SimpleMode(board_size)
        else:
            self.game = GeneralMode(board_size)

        self.board_buttons = []
        self.canvas = None
        self.create_game_widgets()
        self.create_board(board_size)

        # update for letter selected 
        self.set_letter_selection("Red", self.red_letter_choice.get())
        self.set_letter_selection("Blue", self.blue_letter_choice.get())
        self.update_turn_display()
        
        self.game_window.mainloop()

    def set_letter_selection(self, player_color, letter): # new method for sprint #3

        """Sets the selected letter, updates the visual toggle buttons, and updates the display label."""

        if player_color == "Red":
            self.red_letter_choice.set(letter)
            s_button = self.red_s_button
            o_button = self.red_o_button
            display_label = self.red_selection_label
        else:
            self.blue_letter_choice.set(letter)
            s_button = self.blue_s_button
            o_button = self.blue_o_button
            display_label = self.blue_selection_label
        
        # Highlight the selected button to show which was picked
        if letter == "S":
            s_button.config(bg="#A0E0A0", relief=tk.SUNKEN)
            o_button.config(bg="SystemButtonFace", relief=tk.RAISED)
        else:
            s_button.config(bg="SystemButtonFace", relief=tk.RAISED)
            o_button.config(bg="#A0E0A0", relief=tk.SUNKEN)
            
        # Indicates the letter selected for each player during said players turn 
        if display_label:
            display_label.config(text=f"Selected: {letter}", font=("Helvetica", 12, "bold"))
    
    def create_game_widgets(self):
         # turn label 
        turn_frame = tk.Frame(self.game_window, bd=5, relief=tk.RAISED, bg="#20B2AA")
        self.turn_label = tk.Label(turn_frame, text="", font=("Helvetica", 16, "bold"), bg="#FFFAFA")
        self.turn_label.pack(padx=5, pady=5)
        turn_frame.pack(pady=10)

        # Mode label
        mode_frame = tk.Frame(self.game_window, bd=3, relief=tk.RIDGE, bg="#008B8B")
        self.mode_label = tk.Label(mode_frame, text=f"Game Mode: {self.mode.get()}", font=("Helvetica", 14, "bold"), bg="#E0FFFF",fg="black")
        self.mode_label.pack(padx=5, pady=3)
        mode_frame.pack(pady=5)
        
        main_game_area_frame = tk.Frame(self.game_window, bg="#008B8B")
        main_game_area_frame.pack(pady=10)
        
        # Player info (red player)
        red_controls_frame = tk.Frame(main_game_area_frame, bg="#008B8B")
        red_controls_frame.grid(row=0, column=0, padx=20, pady=10, sticky=tk.N)
        
        red_frame = tk.Frame(red_controls_frame, bd=5, relief=tk.RAISED, bg="#DC143C")
        self.red_label = tk.Label(red_frame, text="", bg="#E9967A", fg="black", font=("Helvetica", 14, "bold"))
        self.red_label.pack(padx=10, pady=5)
        red_frame.pack(pady=10)
        
        red_letter_frame = tk.Frame(red_controls_frame, bd=5, relief=tk.RAISED, bg="#20B2AA")
        tk.Label(red_letter_frame, text="Select Move:", bg="#FFFAFA", fg="black").pack(side=tk.TOP, padx=5, pady=5)
        
        # red players toggle button
        self.red_s_button = tk.Button(red_letter_frame, text="S", width=4,
                                        command=lambda: self.set_letter_selection("Red", "S"))
        self.red_o_button = tk.Button(red_letter_frame, text="O", width=4,
                                        command=lambda: self.set_letter_selection("Red", "O"))
        
        self.red_s_button.pack(side=tk.LEFT, padx=5)
        self.red_o_button.pack(side=tk.LEFT, padx=5)
        red_letter_frame.pack(pady=10)


        # red players selection label
        self.red_selection_label = tk.Label(red_controls_frame, text="", bg="#008B8B", fg="#FFFAFA")
        self.red_selection_label.pack(pady=5)


        # for game board 
        self.board_container = tk.Frame(main_game_area_frame, bg="lightblue", bd=5, relief=tk.RAISED)
        self.board_container.grid(row=0, column=1, padx=20, pady=10)
        
        size = self.board_size.get()
        cell_size = 75
        
        self.canvas = tk.Canvas(self.board_container,
                                width=size * cell_size,
                                height=size * cell_size,
                                bg="white",
                                highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)


        # player info (blue player)
        blue_controls_frame = tk.Frame(main_game_area_frame, bg="#008B8B")
        blue_controls_frame.grid(row=0, column=2, padx=20, pady=10, sticky=tk.N)


        blue_frame = tk.Frame(blue_controls_frame, bd=5, relief=tk.RAISED, bg="#0000CD")
        self.blue_label = tk.Label(blue_frame, text="", bg="#1E90FF", fg="black", font=("Helvetica", 14, "bold"))
        self.blue_label.pack(padx=10, pady=5)
        blue_frame.pack(pady=10)


        blue_letter_frame = tk.Frame(blue_controls_frame, bd=5, relief=tk.RAISED, bg="#20B2AA")
        tk.Label(blue_letter_frame, text="Select Move:", bg="#FFFAFA", fg="black").pack(side=tk.TOP, padx=5, pady=5)
        
        # blue players toggle button
        self.blue_s_button = tk.Button(blue_letter_frame, text="S", width=4,
                                        command=lambda: self.set_letter_selection("Blue", "S"))
        self.blue_o_button = tk.Button(blue_letter_frame, text="O", width=4,
                                        command=lambda: self.set_letter_selection("Blue", "O"))


        self.blue_s_button.pack(side=tk.LEFT, padx=5)
        self.blue_o_button.pack(side=tk.LEFT, padx=5)
        blue_letter_frame.pack(pady=10)


        # blue players selection label
        self.blue_selection_label = tk.Label(blue_controls_frame, text="", bg="#008B8B", fg="#FFFAFA")
        self.blue_selection_label.pack(pady=5)
        
        # buttons at the bottom
        button_frame = tk.Frame(self.game_window, bd=5, relief=tk.RAISED, bg="#008B8B")
        tk.Button(button_frame, text="REPLAY GAME", height=2, bg="#FFFAFA", command=self.reset_game).grid(row=0, column=0, padx=4, pady=4)
        tk.Button(button_frame, text="NEW GAME", height=2, bg="#FFFAFA", command=self.start_game_from_setup).grid(row=0, column=1, padx=4, pady=4)
        tk.Button(button_frame, text="EXIT GAME", height=2, bg="#FFFAFA", command=self.game_window.destroy).grid(row=0, column=2, padx=4, pady=4)
        button_frame.pack(pady=10)
    
    def update_player_controls(self): # new method for sprint #3
        """Enable the current players toggle button and disable opponent's"""
        current_player_color = self.game.current_turn.color

        if current_player_color == "Red":
            self.red_s_button.config(state=tk.NORMAL)
            self.red_o_button.config(state=tk.NORMAL)
            self.blue_s_button.config(state=tk.DISABLED)
            self.blue_o_button.config(state=tk.DISABLED)
            self.red_selection_label.config(fg="#FFFAFA")
            self.blue_selection_label.config(fg="#808080")
        else:
            self.blue_s_button.config(state=tk.NORMAL)
            self.blue_o_button.config(state=tk.NORMAL)
            self.red_s_button.config(state=tk.DISABLED)
            self.red_o_button.config(state=tk.DISABLED)
            self.blue_selection_label.config(fg="#FFFAFA")
            self.red_selection_label.config(fg="#808080")

    def create_board(self, size):
        """Creating the button grid for the game board"""

        self.board_buttons = []
        self.canvas.delete("all")
        self.canvas.update_idletasks()
        cell_width = self.canvas.winfo_width() / size
        cell_height = self.canvas.winfo_height() / size

        for i in range(size):
            row_buttons = []
            for j in range(size):
                   button = tk.Button(
                       master=self.canvas,
                       text="",
                       width=6,
                       height=3,
                       bg="white",
                       font=("Helvetica", 16, "bold"), # Corrected font name
                       command=lambda r=i, c=j: self.handle_click(r,c))
                   x_center = j * cell_width + cell_width / 2
                   y_center = i * cell_height + cell_height / 2
                   self.canvas.create_window(x_center, y_center, window=button, anchor=tk.CENTER)
                   row_buttons.append(button)
            # This line is now correctly indented
            self.board_buttons.append(row_buttons)

    def handle_click(self, row, col):
        """Handle the moves on the board"""

        if not self.game or self.game.is_game_over:
            return

        current_player_color = self.game.current_turn.color

        if current_player_color == "Red":
            letter = self.red_letter_choice.get()
        else:
            letter = self.blue_letter_choice.get()


        new_lines_info = self.game.make_move(row, col, letter)

        # to help keep track of moves as lines weren't appearing in game window
        print(f"Move made at ({row}, {col}) with letter '{letter}'")
        print(f"Lines info returned: {new_lines_info}")

        if new_lines_info is not False:

            # changed the letter color to black
            self.board_buttons[row][col].config(text=letter, fg="black")

            if new_lines_info:  # checking if lines were draw
                print(f"Drawing {len(new_lines_info)} lines")
                self.draw_sos_lines(new_lines_info)
            else:
                print("No SOS patterns detected")


            if self.game.is_game_over:
                self.end_game()
            else:
                self.update_turn_display()
        else:
            messagebox.showwarning("Invalid Move", "That cell is already occupied.")
    
    def draw_sos_lines(self, lines_info): # new method for sprint #3
        """Draws lines in the color of the player who scored the SOS."""
        if not lines_info:
            return

        size = self.board_size.get()
        cell_width = 75  # match with the cell size
        cell_height = 75

        for info in lines_info:
            (start_r, start_c), (end_r, end_c), color = info
        
            # calculate the positions corresponding to the canvas coords
            x1 = start_c * cell_width + cell_width / 2
            y1 = start_r * cell_height + cell_height / 2
            x2 = end_c * cell_width + cell_width / 2
            y2 = end_r * cell_height + cell_height / 2

            # make the line
            self.canvas.create_line(x1, y1, x2, y2,
                                    fill=color,
                                    width=6,
                                    tag="sos_line")

        self.canvas.tag_lower("all")
        self.canvas.tag_raise("sos_line")
        self.canvas.update_idletasks()

    def update_turn_display(self):
        """Update the player labels and the turn labels"""

        current_player = self.game.current_turn
        self.turn_label.config(text=f"Current Turn: {current_player.color.upper()}")
        red_score = self.game.SOS_count["Red"]
        blue_score = self.game.SOS_count["Blue"]
        self.red_label.config(text=f"RED PLAYER (R)\nScore: {red_score}")
        self.blue_label.config(text=f"BLUE PLAYER (B)\nScore: {blue_score}")

        self.update_player_controls()
    
    def end_game(self):
        """Determines the winner of game"""
        winner = self.game.determine_winner()

        self.update_turn_display()

        if winner == "Draw": # if draw, update the message of state
            self.turn_label.config(text=f"GAME OVER: IT'S A DRAW!")
            messagebox.showinfo("Game Over", f"The {self.mode.get()} has ended in a Draw!")
        else:
            self.turn_label.config(text=f"GAME OVER: {winner.upper()} WINS!")
            messagebox.showinfo("Game Over", f"The {self.mode.get()} Winner is: {winner.upper()}!")
    
    def reset_game(self):
        """reset the game"""

        if self.game:
            self.game.reset()
        self.canvas.delete("sos_line")
        for row in self.board_buttons:
            for button in row:
                button.config(text="", fg="black", bg="white") 

        self.set_letter_selection("Red", "S")
        self.set_letter_selection("Blue", "S")
        self.update_turn_display()
    
    def start_game_from_setup(self):
        self.game_window.destroy()
        SOSGame()

if __name__ == "__main__":
    SOSGame()