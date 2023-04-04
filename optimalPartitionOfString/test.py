import pytest
from .solution import Solution

@pytest.mark.parametrize("s, expected", [
   ("abacaba", 4),
   ("ssssss", 6),
   ("hdklqkcssgxlvehva", 4)
])
def test(s, expected):
    actual = Solution().partitionString(s)
    assert actual == expected
