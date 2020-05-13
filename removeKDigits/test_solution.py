from typing import List

import pytest

from removeKDigits.solution import Solution


@pytest.mark.parametrize("input, k, expected",
                         [
                             ("1432219", 3, "1219"),
                             ("10", 2, "0"),
                             ("10200", 1, "200"),
                         ])
def test_solution(input, k, expected):
    actual = Solution().removeKdigits(input, k)

    assert actual == expected
