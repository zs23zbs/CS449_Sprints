"""Player Class"""

class Player:
    def __init__(self, color, letter_choice="S"):
        self.color = color
        self.letter_choice = letter_choice
    
    def toggle_letter(self): # for when the toggle changes between S and O letter 
        current_player = Player() 
        current_letter = Player()

        if current_player.letter_choice == "S":
            current_letter.letter_choice = "O"
        elif current_player.letter_choice == "O":
            current_letter.letter_choice = "S"
