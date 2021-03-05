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


def test_factorial():
    assert math_lib.factorial(0) == 1
    assert math_lib.factorial(1) == 1
    assert math_lib.factorial(2) == 2
    assert math_lib.factorial(3) == 6
    assert math_lib.factorial(4) == 24
    assert math_lib.factorial(5) == 120
    assert math_lib.factorial(10) == 3628800


def test_power_regular():
    assert math_lib.power(3, 4) == 81
    assert math_lib.power(3, 5) == 243
    assert math_lib.power(2, 6) == 64
    assert math_lib.power(2, 7) == 128

    for i in range(-10, 10):
        assert math_lib.power(i, 2) == i * i
        assert math_lib.power(i, 3) == i * i * i

        assert math_lib.power(math_lib.power(i, 2), 3) == math_lib.power(i, 6)
        assert math_lib.power(math_lib.power(i, 3), 2) == math_lib.power(i, 6)


def test_power_one():
    for i in range(-10, 10):
        assert math_lib.power(1, i) == 1


def test_power_to_one():
    for i in range(-10, 10):
        assert math_lib.power(i, 1) == i


def test_power_to_zero():
    for i in range(-10, 10):
        assert math_lib.power(i, 0) == 1


def test_nth_root_sqrt():
    assert math_lib.nth_root(1, 2) == 1
    assert math_lib.nth_root(4, 2) == 2
    assert math_lib.nth_root(9, 2) == 3
    assert math_lib.nth_root(16, 2) == 4
    assert math_lib.nth_root(25, 2) == 5
    assert math_lib.nth_root(225, 2) == 15

    with pytest.raises(Exception):
        math_lib.nth_root(-1, 2)


def test_nth_root_regular():
    assert math_lib.nth_root(27, 3) == 3
    assert math_lib.nth_root(64, 3) == 4

    assert math_lib.nth_root(8, 3) == 2
    assert math_lib.nth_root(16, 4) == 2
    assert math_lib.nth_root(32, 5) == 2

    with pytest.raises(Exception):
        math_lib.nth_root(-1, 4)


def test_nth_root_zero():
    for n in range(2, 10):
        assert math_lib.nth_root(0, n) == 0


def test_nth_root_one():
    for n in range(2, 10):
        assert math_lib.nth_root(1, n) == 1


def test_nth_root_odd_negative_one():
    for n in range(3, 11, 2):
        assert math_lib.nth_root(-1, n) == -1


def test_sin_regular():
    assert math_lib.sin(-90) == -1
    assert math_lib.sin(0) == 0
    assert math_lib.sin(90) == 1
    assert math_lib.sin(180) == 0
    assert math_lib.sin(270) == -1
    assert math_lib.sin(360) == 0
    assert math_lib.sin(720) == 0
    assert math_lib.sin(1080) == 0


def test_sin_odd():
    for x in range(0, 360, 10):
        assert math_lib.sin(x) == -math_lib.sin(-x)


def test_cos_regular():
    assert math_lib.cos(-90) == 0
    assert math_lib.cos(0) == 1
    assert math_lib.cos(90) == 0
    assert math_lib.cos(180) == -1
    assert math_lib.cos(270) == 0
    assert math_lib.cos(360) == 1
    assert math_lib.cos(720) == 1
    assert math_lib.cos(1080) == 1


def test_cos_even():
    for x in range(0, 360, 10):
        assert math_lib.cos(x) == math_lib.cos(-x)


def test_tan_regular():
    assert math_lib.tan(-45) == -1
    assert math_lib.tan(0) == 0
    assert math_lib.tan(45) == 1


def test_tan_increasing():
    for x in range(-80, 80, 5):
        assert math_lib.tan(x) < math_lib.tan(x + 5)


def test_tan_odd():
    for x in range(0, 89, 1):
        assert math_lib.tan(x) == -math_lib.tan(-x)


def test_tan_not_defined():
    with pytest.raises(Exception):
        math_lib.tan(90)

    with pytest.raises(Exception):
        math_lib.tan(270)
