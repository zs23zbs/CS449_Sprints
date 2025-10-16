"""Board Class"""
# Represents the grid (2d list of cells)
# Keep track of what is in the ceels (S or O, or empty) 
# Ensure valid moves 
# Is a provided helper funtion for logic and GUI 

class Board:
    def __init__(self, board_size): 
        self.board_size = board_size 
        #Supposed to create a board with input given size and fill it with nothing
