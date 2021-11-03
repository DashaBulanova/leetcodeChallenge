import pytest

from .solution import Solution


@pytest.mark.parametrize("input, k, expected",
                         [
                                 ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
                               ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
                             ([-1], 2, [-1]),
                             ([1, 2], 3, [2, 1]),
                         ])
def test(input, k, expected):
    Solution().rotate(input, k)
    for i in range(len(input)):
        assert input[i] == expected[i]
