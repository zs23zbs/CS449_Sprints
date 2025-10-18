import pytest 
from game_logic import GameLogic

"""AI Generated Automated Tests"""
def test_make_move_and_switch_turn(): 
    game = GameLogic(3, "Simple")

    successful_move = game.make_move(0,0)

    assert successful_move is True
    assert game.board.game_board[0][0]==("S", "Blue")
    assert game.current_turn.color == "Red"