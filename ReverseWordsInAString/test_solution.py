import pytest

from countingBits.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [(2, [0, 1, 1]),
                         (5, [0, 1, 1, 2, 1, 2])])
def test_find_a_peak_index(input, expected):
    actual = Solution().countBits(input)

    assert actual == expected
