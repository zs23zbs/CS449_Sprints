import pytest 
from game_logic import GameLogic
from board_class import Board

"""AI Generated Automated Tests (2)""" 
def test_make_move_and_switch_turn(): 
    game = GameLogic(3, "Simple")

    successful_move = game.make_move(0,0)

    assert successful_move is True
    assert game.board.game_board[0][0]==("S", "Blue")
    assert game.current_turn.color == "Red"

def test_invalid_move_doesnt_change_turn():
    game = GameLogic(3, "Simple")

    game.make_move(0,0)
    previous_turn = game.current_turn.color

    move_is_successful = game.make_move(0,0)

    assert move_is_successful is False
    assert game.current_turn.color == previous_turn

"""More Automated Tests"""
def test_board_creation():
    board = Board(3)

    assert board.board_size == 3
    assert len(board.game_board) == 3
    assert all(cell is None for row in board.game_board for cell in row)

def test_placing_letter_on_empty_cell():
    board = Board(3)
    result = board.place(0, 1, "O", "Blue")
    
    assert result is True
    assert board.game_board[0][1] == ("O", "Blue")

def test_dont_place_on_nonempty_cell():
    board = Board(4)
    board.place(1, 2, "S", "Red")
    result = board.place(1, 2, "O", "Blue")

    assert result is False

def test_turn_changes():
    game = GameLogic(3, "Simple Game")
    first_player = game.current_turn
    game.switch_turn()

    assert game.current_turn != first_player

def test_maing_move_change_turns_and_board():
    game = GameLogic(3, "Simple Game")
    start_turn = game.current_turn
    result = game.make_move(2, 1)
    
    assert result is True
    assert game.board.game_board[2][1][0] in ["S", "O"]
    assert game.current_turn != start_turn

def test_board_resets():
    game = GameLogic(3, "Simple Game")
    game.make_move(1,2)
    game.reset()

    for row in game.board.game_board:
        for cell in row:
            assert cell is None