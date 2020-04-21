import pytest

from PeakIndexInMountainArray import Solution


@pytest.mark.parametrize("input_array,expected",
                         [([0, 1, 0], 1),
                          ([3, 2, 1, 0, 0], 0),
                          ([0, 1, 1, 2, 3], 4),
                          ([0, 1, 0, 3, 4, 5, 10, 9], 6),
                          ([0, 2, 1, 0], 1)])
def test_find_a_peak_index(input_array, expected):
    actual = Solution().peak_index_in_mountain_array(input_array)

    assert actual == expected
