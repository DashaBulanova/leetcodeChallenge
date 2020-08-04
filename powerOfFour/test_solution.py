import pytest

from powerOfFour.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             (16, True),
                             (8, False),
                             (64, True),
                             (81, False),
                             (-256, False),
                             (5, False),
                             (1, True),
                             (4, True)
                          ])
def test_is_palindrome(input, expected):
    actual = Solution().isPowerOfFour(input)
    assert actual == expected
