from game_of_greed import __version__
import pytest
from game_of_greed.game_of_greed import GameLogic, Banker

def test_version():
    assert __version__ == '0.1.0'


def test_single_five():
    actual = GameLogic.calculte_score((5,))
    expected = 50
    assert actual == expected


def test_single_one():
    actual = GameLogic.calculte_score((1,))
    expected = 100
    assert actual == expected


def test_two_fives():
    actual = GameLogic.calculte_score((5, 5))
    expected = 100
    assert actual == expected


def test_two_ones():
    actual = GameLogic.calculte_score((1, 1))
    expected = 200
    assert actual == expected


def test_one_and_five():
    actual = GameLogic.calculte_score((1, 5))
    expected = 150
    assert actual == expected


def test_zilch():
    actual = GameLogic.calculte_score((2,))
    expected = 0
    assert actual == expected


def test_three_fives():
    actual = GameLogic.calculte_score((5, 5, 5, 2, 2, 3))
    expected = 500
    assert actual == expected


def test_three_ones():
    actual = GameLogic.calculte_score((1, 1, 1, 2, 3, 4))
    expected = 1000
    assert actual == expected


def test_three_ones_and_a_five():
    actual = GameLogic.calculte_score((1, 1, 1, 5))
    expected = 1050
    assert actual == expected


def test_straight():
    actual = GameLogic.calculte_score((1, 6, 3, 2, 5, 4))
    expected = 1500
    assert actual == expected


def test_three_of_a_kind():
    actual = GameLogic.calculte_score((2, 2, 2))
    expected = 200
    assert actual == expected


def test_four_of_a_kind():
    actual = GameLogic.calculte_score((2, 2, 2, 2))
    expected = 400
    assert actual == expected


def test_five_of_a_kind():
    actual = GameLogic.calculte_score((2, 2, 2, 2, 2))
    expected = 600
    assert actual == expected


def test_six_of_a_kind():
    actual = GameLogic.calculte_score((2, 2, 2, 2, 2, 2))
    expected = 800
    assert actual == expected


def test_six_ones():
    actual = GameLogic.calculte_score((1, 1, 1, 1, 1, 1))
    expected = 4000
    assert actual == expected

def test_new_banker():
    banker = Banker()
    assert banker.unbanked_points == 0
    assert banker.total == 0


def test_shelf():
    banker = Banker()
    banker.shelf(100)
    assert banker.unbanked_points == 100
    assert banker.total == 0


def test_deposit():
    banker = Banker()
    banker.shelf(100)
    banker.bank()
    assert banker.unbanked_points == 0
    assert banker.total == 100
