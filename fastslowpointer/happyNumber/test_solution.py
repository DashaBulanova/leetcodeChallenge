import pytest
from solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                          (19, True),
                          (2, False),
                          ])
def test(input, expected):
    actual = Solution().isHappy(input)
    assert actual == expected
