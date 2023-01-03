import pytest
from .solution import Solution


@pytest.mark.parametrize("nums, queries, expected", [
    # ([4, 5, 2, 1], [3, 10, 21], [2, 3, 4]),
    # ([2, 3, 4, 5], [1], [0]),
    ([469781, 45635, 628818, 324948, 343772, 713803, 452081], [816646, 929491], [3, 3])
])
def test(nums, queries, expected):
    actual = Solution().answerQueries(nums, queries)
    assert actual == expected
