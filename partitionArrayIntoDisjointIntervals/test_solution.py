import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([5, 0, 3, 8, 6], 3),
                             ([1, 1, 1, 0, 6, 12], 4),
                             ([32, 57, 24, 19, 0, 24, 49, 67, 87, 87], 7),
                             ([26, 51, 40, 58, 42, 76, 30, 48, 79, 91], 1),
                             ([24, 11, 49, 80, 63, 8, 61, 22, 73, 85], 9),
                         ])
def test_solution(input, expected):
    actual = Solution().partitionDisjoint(input)
    assert actual == expected
