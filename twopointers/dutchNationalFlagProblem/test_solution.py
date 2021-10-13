import pytest

from .solution import dutch_flag_sort


@pytest.mark.parametrize("input,  expected",
                         [
                             ([1, 0, 2, 1, 0], [0, 0, 1, 1, 2]),
                             ([2, 2, 0, 1, 2, 0], [0, 0, 1, 2, 2, 2]),
                             ([2, 0, 1], [0, 1, 2]),
                             ([0], [0]),
                             ([1], [1]),
                             ([0, 2, 2, 2, 0, 2, 1, 1], [0, 0, 1, 1, 2, 2, 2, 2]),
                         ])
def test_number_of_bits(input, expected):
    dutch_flag_sort(input)
    assert input == expected
