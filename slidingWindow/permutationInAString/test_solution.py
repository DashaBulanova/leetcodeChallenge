import pytest

from .solution import Solution


@pytest.mark.parametrize("input, pattern, expected",
                         [
                             ("oidbcaf", "abc", True),
                             ("odicf", "dc", False),
                             ("bcdxabcdy", "bcdyabcdx", True),
                             ("aaacb", "abc", True),
                         ])
def test_number_of_bits(input, pattern, expected):
    actual = Solution().find_permutation(input, pattern)
    assert actual == expected
