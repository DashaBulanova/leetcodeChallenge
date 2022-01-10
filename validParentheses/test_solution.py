import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False)
])
def test(input, expected):
    actual = Solution().isValid(input)
    assert actual == expected
