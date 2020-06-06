import pytest

from queueReconstructionByHeight.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
                              [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]),
                         ])
def test_bst_to_gst(input, expected):
    actual = Solution().reconstructQueue(input)
    assert actual == expected
