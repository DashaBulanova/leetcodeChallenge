import pytest

from stringCompression.solution import Solution


@pytest.mark.parametrize("input, expected_len, expected", [
    (["a", "a", "b", "b", "c", "c", "c"], 6, ["a", "2", "b", "2", "c", "3"]),
    (["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], 4, ["a", "b", "1", "2"]),
    (["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "a"], 4, ["b", "1", "2", "a"])
])
def test(input, expected_len, expected):
    actual = Solution().compress(input)
    assert expected_len == actual
    assert expected == input


"""
1 ~ 0 = 1
0 ~ 1 = 1
1 ~ 1 = 0
0 ~ 0 = 0

  001 = 1
~ 010 = 2
~ 001 = 1
~ 011 = 3
~ 010 = 2
~ 101 = 5
~ 110 = x~y




"""
