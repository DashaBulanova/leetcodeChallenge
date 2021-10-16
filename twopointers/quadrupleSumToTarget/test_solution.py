import pytest

from .solution import search_quadruplets


@pytest.mark.parametrize("input, target, expected",
                         [
                             #  ([4, 1, 2, -1, 1, -3], 1, [[-3, -1, 1, 4], [-3, 1, 1, 2]]),
                              ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
                             ([-2, -1, -1, 1, 1, 2, 2], 0, [[-2, -1, 1, 2], [-1, -1, 1, 1]]),
                             # -2 -1 -1 1 1 2 2
                         ])
def test_number_of_bits(input, target, expected):
    actual = search_quadruplets(input, target)
    assert actual == expected
