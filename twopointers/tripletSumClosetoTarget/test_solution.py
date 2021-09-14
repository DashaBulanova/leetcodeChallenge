import pytest

from .solution import triplet_sum_close_to_target


@pytest.mark.parametrize("input, target, expected",
                         [
                             ([-2, 0, 1, 2], 2, 1),
                             ([1, 0, 1, 1], 100, 3),
                             ([-3, -1, 1, 2], 1, 0),
                         ])
def test(input, target, expected):
    actual = triplet_sum_close_to_target(input, target)
    assert actual == expected