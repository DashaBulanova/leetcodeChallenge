import pytest

from .solution import Solution


@pytest.mark.parametrize("intervals, newInterval, expected", [
      ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
     ([[1, 3], [6, 9]], [2, 3], [[1, 3], [6, 9]]),
     ([[1, 3], [6, 9]], [10, 11], [[1, 3], [6, 9], [10, 11]]),
      ([[2, 3], [6, 9]], [0, 1], [[0, 1], [2, 3], [6, 9]]),
    ([[0, 5], [9, 12]], [7, 16], [[0, 5], [7, 16]]),
     ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]])
])
def test(intervals, newInterval, expected):
    actual = Solution().insert(intervals, newInterval)
    assert actual == expected

# @pytest.mark.parametrize("intervals, value, expected", [
#        ([1, 6], 2, 0),
#        ([3, 9], 5, 0),
#      #    ([1, 3, 4, 5, 6, 8], 6, 4),
#      #   ([1, 3, 4, 5, 6, 8], 7, 4),
#      #    ([1, 3, 4, 5, 6, 8], 0, -1),
#      # ([1, 3, 4, 5, 6, 8], 9, 6),
# ])
# def test(intervals, value, expected):
#     actual = Solution().define_pointer(intervals, value, 0, len(intervals)-1)
#     assert actual == expected
