import pytest

from validPalindrome.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ("A man, a plan, a canal: Panama", True),
                             ("race a car", False),
                             ("0P", False)
                          ])
def test_is_palindrome(input, expected):
    actual = Solution().isPalindrome(input)
    assert actual == expected
