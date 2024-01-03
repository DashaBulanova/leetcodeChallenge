import pytest
from .solution import Solution

@pytest.mark.parametrize("bank, expected", [
    (["011001","000000","010100","001000"], 8),
    ( ["000","111","000"], 0)
])
def test(bank, expected):
    actual = Solution().numberOfBeams(bank)
    assert actual == expected