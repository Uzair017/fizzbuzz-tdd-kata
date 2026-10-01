# import pytest

# from fizzbuzz_tdd_kata.core import fizzbuzz

# @pytest.mark.parametrize(
#     ("n", "expected"),
#     [
#         (1, "1"),
#         (2, "2"),
#         (3, "Fizz"),
#         (5, "Buzz"),
#         (6, "Fizz"),
#         (10, "Buzz"),
#         (15, "FizzBuzz"),
#         (30, "FizzBuzz"),
#         (100, "Buzz"),
#     ],
# )
# def test_cases(n, expected):
#     assert fizzbuzz(n) == expected

# @pytest.mark.parametrize("n", [0,-1,-5])
# def test_fizzbuzz_rejects_invalid_num(n):
#     with pytest.raises(ValueError):
#         fizzbuzz(n)

import pytest

from fizzbuzz_tdd_kata.core import fizzbuzz


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, "1"),
        (2, "2"),
        (3, "Fizz"),
        (5, "Buzz"),
        (6, "Fizz"),
        (10, "Buzz"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
        (100, "Buzz"),
    ],
)
def test_cases(n, expected):
    assert fizzbuzz(n) == expected


@pytest.mark.parametrize("n", [0, -1, -5])
def test_fizzbuzz_rejects_invalid_num(n):
    with pytest.raises(ValueError):
        fizzbuzz(n)
