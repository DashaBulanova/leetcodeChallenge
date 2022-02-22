import pytest
from .solution import Solution

@pytest.mark.parametrize("input, expected",[
("A", 1),
("AB",28),
("ZY", 701),
("ZZ", 702),
("AAA",703)
])
def test(input, expected):
    actual = Solution().titleToNumber(input)
    assert actual == expected
