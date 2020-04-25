import pytest

from bitwiseAndOfNumbersRange.solution import Solution


@pytest.mark.parametrize("m,n, expected",
                         [
                          # ("()", True),
                          # ("(*)", True),
                          # ("(*))", True),
                          (5,7,4),
                          (4,7,4),
                          (6,7,6),
                          (27,31,24),
                          (600000000,2147483645,0),
                          #("(*(*", True),
                        ])
def test_solution(m,n, expected):
    actual = Solution().rangeBitwiseAnd(m,n)
    assert actual == expected
