import pytest 
from board_class import Board
from player_class import ComputerPlayer
import random

# All Test Cases pass

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

def test_computer_find_vertical_win():
    """Tests for Computer player to make a vertical S-O-S win"""

    # set up board object
    board = Board(6)
    computer_player = ComputerPlayer("Blue")

    # Set up the winning (vertical) pattern
    board.place(3, 2, "S", "Red")
    board.place(4, 2, "O", "Blue")

    move = computer_player.get_move(board)

    # Assert that the move is completed
    assert move == (5, 2, "S")

def test_computer_does_random_move(monkeypatch):
    """Tests the computer player to make a random move when no immediate SOS can be done"""

    board = Board(3) 
    computer_player = ComputerPlayer("Red")

    # Fill two cells for no accident wins
    board.place(0, 0, "O", "Red")
    board.place(2, 2, "0", "Blue")

    # Mock random to pick a predictable move (0, 1, "S")
    def mock_choice(seq):
        return (0, 1, "S")
    
    monkeypatch.setattr(random, "choice", mock_choice)

    move = computer_player.get_move(board)

    # Assert that the move is the one the mocked random returns 
    assert move == (0, 1, "S")
    assert board.is_cell_empty(0,1)

def test_computer_full_board():
    """Tests the computer player to return None if the board is full """

    board = Board(4)
    computer_player = ComputerPlayer("Red")

    # Fill all the cells in the board
    for r in range(4):
        for c in range(4):
            board.place(r, c, "O", "Red")
    
    # Assert board is all full 
    assert board.is_full() == True

    move = computer_player.get_move(board)

    # Assert that no move is returned 
    assert move is None