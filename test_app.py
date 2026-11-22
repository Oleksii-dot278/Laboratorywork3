import pytest
from app import Figure


def test_triangle():
    assert Figure("трикутник", 5).get_angles == 3


def test_square():
    assert Figure("квадрат", 5).get_angles == 4


def test_rectangle():
    assert Figure("прямокутник", 5).get_angles == 4


def test_invalid_length():
    with pytest.raises(AssertionError):
        Figure("квадрат", 0)


def test_invalid_type():
    with pytest.raises(AssertionError):
        Figure("коло", 5)


def test_unreachable_fallback():
    fig = Figure("квадрат", 5)
    fig.type = "коло"  # обходимо перевірку в __init__
    assert fig.get_angles == 0

def test_no_assert():
    Figure("квадрат", 5).get_angles

def test_with_assert():
    assert Figure("квадрат", 5).get_angles == 4
    