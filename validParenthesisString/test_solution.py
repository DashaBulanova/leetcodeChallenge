import pytest

from validParenthesisString.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                          # ("()", True),
                          # ("(*)", True),
                          # ("(*))", True),
                          ("(*)(", False)
                          #("(*(*", True),
                        ])
def test_solution(input, expected):
    actual = Solution().checkValidString(input)
    assert actual == expected
