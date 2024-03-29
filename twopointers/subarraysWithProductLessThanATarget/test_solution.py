import pytest

from .solution import find_subarrays


@pytest.mark.parametrize("input, target, expected",
                         [
                             ([2, 5, 3, 10], 30, [[2], [2, 5], [5], [5, 3], [3], [10]]),
                             ([8, 2, 6, 5], 50, [[8], [8, 2], [2], [2, 6], [6], [6, 5], [5]]),
                             ([10, 5, 2, 6], 100, [[10], [10, 5], [5], [5, 2], [2], [5, 2, 6], [2, 6], [6]]),
                         ])
def test(input, target, expected):
    actual = find_subarrays(input, target)
    assert actual == expected
