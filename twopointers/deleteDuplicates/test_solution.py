import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([2, 3, 3, 3, 6, 9, 9], [2, 3, 6, 9]),
                             ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
                         ])
def test(input, expected):
    actual = Solution().remove_duplicates(input)

    assert actual == len(expected)
    for i in range(0, len(expected)):
        assert input[i] == expected[i]
