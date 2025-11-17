import pytest 
from board_class import Board
from player_class import ComputerPlayer

def test_computer_finds_horizontal_win():
    """Tests for Computer player to make a S-O-S horizontal win"""

    # Set up board objects
    board = Board(3) 
    computer_player = ComputerPlayer("Red")

    # Create the winning pattern 
    board.place(0, 0, "S", "Blue")
    board.place(0, 1, "O", "Red")

    move = computer_player.get_move(board)

    # Assert that the move is completed
    assert move == (0, 2, "S")