import pytest

from findTheTownJudge.solution import Solution


@pytest.mark.parametrize("N, trust, expected",
                         [
                             (2, [[1, 2]], 2),
                             (3, [[1, 3], [2, 3]], 3),
                             (3, [[1, 3], [2, 3], [3, 1]], -1),
                             (3, [[1, 2], [2, 3]], -1),
                             (4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]], 3)
                         ])
def test_number_of_bits(N, trust, expected):
    actual = Solution().findJudge(N, trust)
    assert actual == expected
