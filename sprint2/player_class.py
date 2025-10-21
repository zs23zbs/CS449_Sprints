"""Player Class"""

class Player:
    def __init__(self, color, letter_choice="S"):
        """Initialize Player objects
        
        Args: 
        color (str): The color for identifying players (Red or Blue)
        letter_choice (str): The letter or label that players use to play SOS game (S or O) 
        """
        
        self.color = color
        self.letter_choice = letter_choice