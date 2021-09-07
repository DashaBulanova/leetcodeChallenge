import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ('(()', 2),
                             ('()', 2),
                             (")()())", 4),
                             (')()())', 4),
                             ('(()()', 4),
                             ('(()(()()', 4),
                         ])
def test_number_of_bits(input, expected):
    actual = Solution().longestValidParentheses(input)
    assert actual == expected
