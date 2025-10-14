"""Player Class"""

class Player:
    def __init__(self, color, letter_choice="S"):
        self.color = color
        self.letter_choice = letter_choice
    
    def toggle_letter(self): # for when the toggle changes between S and O letter 
        pass
        # Has to check what the current letter choice is 
        # if current letter is S, then must change to O 
        # if current letter is O, then change to S 
        