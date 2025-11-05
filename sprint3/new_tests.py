import pytest
from new_game_logic import SimpleMode as SimpleGameLogic, GeneralMode as GeneralGameLogic
from new_board_class import Board

def test_invalid_move_doesnt_change_turn():
    """Tests making a move on an occupied cell and verifies the turn remains the same"""
    game = SimpleGameLogic(3)
    game.make_move(0,0, "S") # If blue moves then switch to red 
    previous_turn = game.current_turn.color # Red
    move_is_successful = game.make_move(0,0, "S") # red makes move on same cell

    assert move_is_successful is False
    assert game.current_turn.color == previous_turn # turn must remain on red

def test_board_resets():
    """Tests the game reset function"""
    game = SimpleGameLogic(3)
    game.make_move(1,2, "O")
    game.reset()

    # Check if the board is empty
    for row in game.board.game_board:
        for cell in row:
            assert cell is None
    # Check if the turn reset
    assert game.current_turn.color == "Blue"

def test_board_creation_and_turn():
    """Tests initial board state and correct starting turn"""
    game = SimpleGameLogic(3)
    assert game.board.board_size == 3
    assert game.current_turn.color == "Blue" # blue player always starts
    assert game.SOS_count["Red"] == 0 and game.SOS_count["Blue"] == 0

def test_simple_game_make_move_and_switch_turn():
    """Tests if a valid move is made and the turn switches"""
    game = SimpleGameLogic(3)
    game.make_move(0,0, "S") # blue makes a move
    assert game.board.game_board[0][0][0] == "S"
    assert game.current_turn.color == "Red" # switch turns

def test_simple_mode_win_on_first_sos():
    """Test game ends with first SOS"""
    game = SimpleGameLogic(3)
    game.make_move(0, 0, "S") # blue -> red
    game.make_move(0, 1, "O") # red -> blue
    game.make_move(0, 2, "S") # blue scores -> wins
    
    assert game.is_game_over is True
    assert game.SOS_count["Blue"] == 2
    assert game.determine_winner() == "Blue"

def test_simple_mode_draw_no_sos():
    """Test game ends with a draw if board is full with no one scoring"""
    game = SimpleGameLogic(3)
    
    # Fill board without scoring
    game.make_move(0, 0, "S"); game.make_move(0, 1, "O"); game.make_move(0, 2, "O")
    game.make_move(1, 0, "S"); game.make_move(1, 1, "S"); game.make_move(1, 2, "S")
    game.make_move(2, 0, "O"); game.make_move(2, 1, "S"); game.make_move(2, 2, "O")
    
    assert game.board.is_full() is True
    assert game.is_game_over is True
    assert game.determine_winner() == "Draw"

def test_general_mode_turn_does_not_switch_on_score():
    """Test turn doesn't switch if a player scores"""
    game = GeneralGameLogic(4)
    game.make_move(0, 0, "S") # b -> r
    game.make_move(0, 1, "O") # r -> b
    game.make_move(0, 2, "S") # blue scores
    
    assert game.SOS_count["Blue"] == 2
    assert game.is_game_over is False # game continues
    assert game.current_turn.color == "Blue" # turn does NOT switch

def test_general_mode_end_and_winner():
    """Test game ends when full, winner has highest score"""
    game = GeneralGameLogic(4)
    game.make_move(0, 0, "S"); game.make_move(0, 1, "O"); game.make_move(0, 2, "S") # blue scores 2, b's turn
    game.make_move(1, 0, "S") # blue's 2nd move -> r's turn
    game.make_move(2, 0, "S"); game.make_move(2, 1, "O"); game.make_move(2, 2, "S") # red scores 2, r's turn

    # temp/mock board full to check winner
    game.board.is_full = lambda: True
    game.check_game_over()

    assert game.is_game_over is True
    assert game.SOS_count["Blue"] == 2
    assert game.SOS_count["Red"] == 2
    assert game.determine_winner() == "Draw"