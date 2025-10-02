# Tests for functions.py for Tic-Tac-Toe Game
# Created by Aleksej Patkevič <opat74@gmail.com>

import pytest
from unittest.mock import patch
from functions import *

@pytest.fixture
def empty_ground():
    return {
        1: {'A': 'EMPTY_CELL', 'B': 'EMPTY_CELL', 'C': 'EMPTY_CELL'},
        2: {'A': 'EMPTY_CELL', 'B': 'EMPTY_CELL', 'C': 'EMPTY_CELL'},
        3: {'A': 'EMPTY_CELL', 'B': 'EMPTY_CELL', 'C': 'EMPTY_CELL'}
    }

def test_valid_coord():
    expected = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
    assert valid_coord() == expected

def test_make_turn(empty_ground):
    updated = make_turn('X', '2B', empty_ground)
    assert updated[2]['B'] == 'X'

def test_detect_win_row():
    ground = {
        1: {'A': 'X', 'B': 'X', 'C': 'X'},
        2: {'A': 'EMPTY_CELL', 'B': 'O', 'C': 'O'},
        3: {'A': 'O', 'B': 'EMPTY_CELL', 'C': 'X'}
    }
    assert detect_win_row(ground) is True

def test_detect_win_column():
    ground = {
        1: {'A': 'O', 'B': 'X', 'C': 'EMPTY_CELL'},
        2: {'A': 'O', 'B': 'X', 'C': 'EMPTY_CELL'},
        3: {'A': 'EMPTY_CELL', 'B': 'X', 'C': 'EMPTY_CELL'}
    }
    assert detect_win_column(ground) is True

def test_detect_win_diagonals():
    ground = {
        1: {'A': 'X', 'B': 'O', 'C': 'O'},
        2: {'A': 'EMPTY_CELL', 'B': 'X', 'C': 'O'},
        3: {'A': 'O', 'B': 'EMPTY_CELL', 'C': 'X'}
    }
    assert detect_win_diagonals(ground) is True

def test_read_turn_valid(empty_ground):
    with patch('builtins.input', return_value='2B'):
        result = read_turn('X', empty_ground)
        assert result == '2B'

def test_read_turn_quit(empty_ground):
    with patch('builtins.input', return_value='quit'):
        result = read_turn('O', empty_ground)
        assert result == 'QUIT_GAME'