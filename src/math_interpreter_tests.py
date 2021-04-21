import math_interpreter
import math_lib
import pytest


def test_two_members_sum():
    for i in range(-3, 3):
        for j in range(-3, 3):
            assert math_interpreter.eval([i, j], ["+"]) == math_lib.sum(i, j)


def test_two_members_subtraction():
    for i in range(-3, 3):
        for j in range(-3, 3):
            assert math_interpreter.eval([i, j], ["-"]) == math_lib.sub(i, j)


def test_two_members_multiplication():
    for i in range(-3, 3):
        for j in range(-3, 3):
            assert math_interpreter.eval([i, j], ["*"]) == math_lib.multiply(i, j)


def test_two_members_division():
    for i in range(-3, 3):
        for j in range(-3, 3):
            if j == 0:
                continue
            assert math_interpreter.eval([i, j], ["/"]) == math_lib.divide(i, j)


def test_two_members_power():
    for i in range(-3, 3):
        for j in range(1, 6):
            assert math_interpreter.eval([i, j], ["power"]) == math_lib.power(i, j)


def test_two_members_root():
    for i in range(0, 10):
        for j in range(1, 10):
            assert math_interpreter.eval([j, i], ["root"]) == math_lib.nth_root(i, j)


def test_division_by_zero():
    with pytest.raises(Exception):
        math_interpreter.eval([10, 0], ["/"])


def test_invalid_nth_root_base():
    with pytest.raises(ValueError):
        math_interpreter.eval([0, 10], ["root"])

    with pytest.raises(ValueError):
        math_interpreter.eval([1.5, 10], ["root"])


def test_invalid_power_exp():
    with pytest.raises(ValueError):
        math_interpreter.eval([5, 0.5], ["power"])


def test_tree_members_sum():
    for i in range(-3, 3):
        for j in range(-3, 3):
            for k in range(-3, 3):
                assert math_interpreter.eval([i, j, k], ["+", "+"]) == math_lib.sum(math_lib.sum(i, j), k)


def test_tree_members_subtraction():
    for i in range(-3, 3):
        for j in range(-3, 3):
            for k in range(-3, 3):
                assert math_interpreter.eval([i, j, k], ["-", "-"]) == math_lib.sub(math_lib.sub(i, j), k)


def test_tree_members_multiplication():
    for i in range(-3, 3):
        for j in range(-3, 3):
            for k in range(-3, 3):
                assert math_interpreter.eval([i, j, k], ["*", "*"]) == math_lib.multiply(math_lib.multiply(i, j), k)


def test_tree_members_division():
    for i in range(-3, 3):
        for j in range(-3, 3):
            if j == 0:
                continue
            for k in range(-3, 3):
                if k == 0:
                    continue
                assert math_interpreter.eval([i, j, k], ["/", "/"]) == math_lib.divide(math_lib.divide(i, j), k)


def test_multiple_same_priority_operations():
    for i in range(-3, 3):
        for j in range(-3, 3):
            for k in range(-3, 3):
                assert math_interpreter.eval([i, j, k], ["+", "-"]) == math_lib.sub(math_lib.sum(i, j), k)
                assert math_interpreter.eval([i, j, k], ["-", "+"]) == math_lib.sum(math_lib.sub(i, j), k)

    for i in range(-3, 3):
        for j in range(-3, 3):
            for k in range(-3, 3):
                if k == 0:
                    continue
                assert math_interpreter.eval([i, j, k], ["*", "/"]) == math_lib.divide(math_lib.multiply(i, j), k)
                assert math_interpreter.eval([i, k, j], ["/", "*"]) == math_lib.multiply(math_lib.divide(i, k), j)


def test_different_operations_priority():
    for i in range(-3, 3):
        for j in range(-3, 3):
            for k in range(-3, 3):
                # Tests with multiplication
                assert math_interpreter.eval([i, j, k], ["*", "+"]) == math_lib.sum(math_lib.multiply(i, j), k)
                assert math_interpreter.eval([i, j, k], ["*", "-"]) == math_lib.sub(math_lib.multiply(i, j), k)
                assert math_interpreter.eval([i, j, k], ["+", "*"]) == math_lib.sum(i, math_lib.multiply(j, k))
                assert math_interpreter.eval([i, j, k], ["-", "*"]) == math_lib.sub(i, math_lib.multiply(j, k))

                if k == 0:
                    continue

                # Tests with division
                assert math_interpreter.eval([i, j, k], ["+", "/"]) == math_lib.sum(i, math_lib.divide(j, k))
                assert math_interpreter.eval([i, j, k], ["-", "/"]) == math_lib.sub(i, math_lib.divide(j, k))

                assert math_interpreter.eval([i, k, j], ["/", "+"]) == math_lib.sum(math_lib.divide(i, k), j)
                assert math_interpreter.eval([i, k, j], ["/", "-"]) == math_lib.sub(math_lib.divide(i, k), j)
