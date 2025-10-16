"""Player Class"""

class Player:
    def __init__(self, color, letter_choice="S"):
        self.color = color
        self.letter_choice = letter_choice
    
    def toggle_letter(self): # for when the toggle changes between S and O letter 
        # Has to check what the current letter choice is 
        # if current letter is S, then must change to O 
        # if current letter is O, then change to S 

        if self.letter_choice == "S":
            self.letter_choice = "O"
        elif self.letter_choice == "O":
            self.letter_choice = "S"

        return self.letter_choice
    
    def __str__(self): # Just to help with debugging, prints out when passing through the class 
        return f"{self.color} player placing {self.letter_choice}"

