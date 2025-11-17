import pytest 
from board_class import Board
from player_class import ComputerPlayer

def test_computer_finds_horizontal_win():
    """Tests for Computer player to make a S-O-S horizontal win"""

    # Set up board objects
    board = Board(3) 
    computer_player = ComputerPlayer("Red")

    # Create the winning (horizontal) pattern 
    board.place(0, 0, "S", "Blue")
    board.place(0, 1, "O", "Red")

    move = computer_player.get_move(board)

    # Assert that the move is completed
    assert move == (0, 2, "S")

def test_computer_find_diagonal_win():
    """Tests for Computer player to make an S-O-S diagonal win"""

    # Set up the board 
    board = Board(5)
    computer_player = ComputerPlayer("Red")

    # set up the winning (diagonal) pattern 
    board.place(1, 1, "S", "Blue")
    board.place(2, 2, "O", "Red")

    move = computer_player.get_move(board)

    # Assert that the move is completed
    assert move == (3, 3, "S")

def test_computer_player_find_vertical_win():
    """Tests for Computer player to make a vertical S-O-S win"""

    # set up board object
    board = Board(6)
    computer_player = ComputerPlayer("Blue")

    # Set up the winning (vertical) pattern
    board.place(5, 2, "S", "Red")
    board.place(5, 3, "O", "Blue")

    move = computer_player.get_move(board)

    # Assert that the move is completed
    assert move == (5, 4, "S")