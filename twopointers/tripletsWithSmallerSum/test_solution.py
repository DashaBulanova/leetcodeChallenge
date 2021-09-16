import pytest

from .solution import triplet_with_smaller_sum


@pytest.mark.parametrize("input, target, expected",
                         [
                             ([-1, 0, 2, 3], 3, 2),
                             ([-1, 4, 2, 1, 3], 5, 4),
                         ])
def test(input, target, expected):
    actual = triplet_with_smaller_sum(input, target)
    assert actual == expected