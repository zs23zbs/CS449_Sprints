import pytest
from new_game_logic import SimpleMode as SimpleGameLogic, GeneralMode as GeneralGameLogic
from new_board_class import Board

def test_invalid_move_doesnt_change_turn():
    """Tests making a move on an occupied cell and verifies the turn remains the same."""
    game = SimpleGameLogic(3)
    game.make_move(0,0, "S") # If blue moves then switch to red 
    previous_turn = game.current_turn.color # Red
    move_is_successful = game.make_move(0,0, "S") # red makes move on same cell

    assert move_is_successful is False
    assert game.current_turn.color == previous_turn # turn must remain on red

def test_board_resets():
    """Tests the game reset function."""
    game = SimpleGameLogic(3)
    game.make_move(1,2, "O")
    game.reset()

    # Check if the board is empty
    for row in game.board.game_board:
        for cell in row:
            assert cell is None
    # Check if the turn reset
    assert game.current_turn.color == "Blue"