import pytest

from firstUniqueCharacterInAString.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [("leetcode", 0),
                          ("loveleetcode", 2)
                          ])
def test_number_of_bits(input, expected):
    actual = Solution().firstUniqChar(input)
    assert actual == expected
