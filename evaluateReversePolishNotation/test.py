import pytest
from .solution import Solution


@pytest.mark.parametrize("tokens, expected", [
    (["2", "1", "+", "3", "*"], 9),
    (["4", "13", "5", "/", "+"], 6),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22)
])
def test(tokens, expected):
    actual = Solution().evalRPN(tokens)
    assert actual == expected


"""
q=0

i=0
q={4}

i=1, q={4,13}
i=2, q={4,13,5}
i=3 
f=5
"""
