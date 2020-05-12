from typing import List

import pytest

from singleElementInASortedArray.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
                             ([3, 3, 7, 7, 10, 11, 11], 10),
                             ([1, 1, 2, 3, 3], 2)
                         ])
def test_solution(input, expected):
    actual = Solution().singleNonDuplicate(input)

    assert actual == expected
