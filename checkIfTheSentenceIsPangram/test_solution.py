import pytest
from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [("thequickbrownfoxjumpsoverthelazydog", True),
                          ("leetcode", False)
                          ])
def test_number_of_bits(input, expected):
    actual = Solution().checkIfPangram(input)
    assert actual == expected
