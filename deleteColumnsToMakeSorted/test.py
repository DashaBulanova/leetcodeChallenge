import pytest
from .solution import Solution


@pytest.mark.parametrize("strs, expected", [
    (["cba", "daf", "ghi"], 1),
    (["a", "b"], 0),
    (["zyx", "wvu", "tsr"], 3)
])
def test(strs, expected):
    actual = Solution().minDeletionSize(strs)
    assert actual == expected
