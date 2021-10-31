import pytest

from .solution import Solution


@pytest.mark.parametrize("input, k, expected",
                         [
                             ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
                         ])
def test(input, k, expected):
    Solution().rotate(input, k)
    for i in range(len(input)):
        assert input[i] == expected[i]
