import pytest

from .solution import Solution


@pytest.mark.parametrize("input, val, expected",
                         [
                             ([3, 2, 2, 3], 3, [2, 2]),
                             ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),
                         ])
def test(input, val, expected):
    actual = Solution().removeElement(input, val)

    assert actual == len(expected)
    for i in range(0, len(expected)):
        assert input[i] == expected[i]
