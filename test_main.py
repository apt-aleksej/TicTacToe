# Tests for the Tic-Tac-Toe Console Game
# Created by Aleksej Patkevič <opat74@gmail.com>

import pytest
from io import StringIO
from contextlib import redirect_stdout
from main import decide_win, show


@pytest.mark.parametrize("ground,expected", [
    # Victory by row
    ({"1a": " X ", "1b": " X ", "1c": " X ",
      "2a": " . ", "2b": " . ", "2c": " . ",
      "3a": " . ", "3b": " . ", "3c": " . "}, True),

    # Victory by column
    ({"1a": " O ", "2a": " O ", "3a": " O ",
      "1b": " . ", "2b": " . ", "3b": " . ",
      "1c": " . ", "2c": " . ", "3c": " . "}, True),

    # Victory diagonally from left to right
    ({"1a": " X ", "2b": " X ", "3c": " X ",
      "1b": " . ", "1c": " . ", "2a": " . ",
      "2c": " . ", "3a": " . ", "3b": " . "}, True),

    # Victory diagonally from right to left
    ({"3a": " O ", "2b": " O ", "1c": " O ",
      "1a": " . ", "1b": " . ", "2a": " . ",
      "2c": " . ", "3b": " . ", "3c": " . "}, True),

    # No victory
    ({"1a": " X ", "1b": " O ", "1c": " X ",
      "2a": " O ", "2b": " X ", "2c": " O ",
      "3a": " O ", "3b": " X ", "3c": " O "}, False),
])
def test_decide_win(ground, expected):
    assert decide_win(ground) == expected


def test_show_output():
    ground = {
        '1a': ' X ', '1b': ' O ', '1c': ' . ',
        '2a': ' . ', '2b': ' X ', '2c': ' . ',
        '3a': ' O ', '3b': ' . ', '3c': ' X '
    }
    expected_output = (
        "_____A___B___C___\n"
        "1 |  X   O   .  |\n"
        "2 |  .   X   .  |\n"
        "3 |  O   .   X  |\n"
        "_________________\n"
    )

    f = StringIO()
    with redirect_stdout(f):
        show(ground)
    output = f.getvalue()
    assert output == expected_output