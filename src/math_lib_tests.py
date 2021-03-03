import pytest
import math_lib


def test_sum_regular():
    assert math_lib.sum(1, 2) == 3
    assert math_lib.sum(1, 1) == 2
    assert math_lib.sum(0, 0) == 0
    assert math_lib.sum(0, 7) == 7


def test_sum_negative():
    assert math_lib.sum(-1, 1) == 0
    assert math_lib.sum(-4, -4) == -8
    assert math_lib.sum(-8, 4) == -4
    assert math_lib.sum(8, -4) == 4


def test_sub_regular():
    assert math_lib.sub(10, 5) == 5
    assert math_lib.sub(5, 5) == 0
    assert math_lib.sub(10, 15) == -5


def test_sub_negative():
    assert math_lib.sub(5, -5) == 10
    assert math_lib.sub(-5, -5) == 0
    assert math_lib.sub(-10, 15) == -25
    assert math_lib.sub(-10, -5) == -5
    assert math_lib.sub(-10, -20) == 10


def test_multiply_regular():
    assert math_lib.multiply(3, 3) == 9
    assert math_lib.multiply(2, 3) == 6
    assert math_lib.multiply(3, 2) == 6


def test_multiply_negative():
    assert math_lib.multiply(-2, -4) == 8
    assert math_lib.multiply(-3, 5) == -15
    assert math_lib.multiply(4, -4) == -16


def test_multiply_by_one():
    for i in range(1, 10):
        assert math_lib.multiply(i, 1) == i


def test_multiply_by_negative_one():
    for i in range(1, 10):
        assert math_lib.multiply(i, -1) == -i


def test_multiply_by_zero():
    for i in range(1, 10):
        assert math_lib.multiply(i, 0) == 0


def test_divide_regular():
    assert math_lib.divide(10, 2) == 5
    assert math_lib.divide(10, -2) == -5
    assert math_lib.divide(-20, 10) == -2
    assert math_lib.divide(-20, -10) == 2


def test_divide_same_numbers():
    for i in range(-10, 10):
        if i == 0:
            continue
        assert math_lib.divide(i, i) == 1


def test_divide_by_one():
    for i in range(-10, 10):
        assert math_lib.divide(i, 1) == i


def test_divide_by_zero():
    with pytest.raises(Exception):
        math_lib.divide(10, 0)

    with pytest.raises(Exception):
        math_lib.divide(0, 0)
