import pytest

from kthLargestElementInAnArray.solution import Solution


@pytest.mark.parametrize("input, k, expected",
                         [
                             ([3, 2, 1, 5, 6, 4], 2, 5),
                             ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
                             ([3, 2, 3, 1, 2, 4, 5, 5, 6], 8, 2),
                             ([1], 1, 1),
                             ([-1, 2, 0], 2, 0),
                             ([7, 6, 5, 4, 3, 2, 1], 5, 3),
                         ])
def test_bst_to_gst(input, k, expected):
    actual = Solution().findKthLargest(input, k)
    assert actual == expected
