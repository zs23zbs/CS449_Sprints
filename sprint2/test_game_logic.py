import pytest 
from game_logic import GameLogic

"""AI Generated Automated Tests""" # Make sure, correlate to acceptance criteria and user stories from sprint #1 
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

"""Need to make more, keep in mind for making notes on Sprint #2 Report"""
# Note, make sure the terminal is in same directory as "sprint2" using cd and ls