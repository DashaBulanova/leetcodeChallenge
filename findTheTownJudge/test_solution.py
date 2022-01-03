import pytest
from .solution import Solution

@pytest.mark.parametrize("n, trust, expected", [
(2, [[1,2]], 2),
(3, [[1,3],[2,3]], 3),
(3, [[1,3],[2,3],[3,1]], -1),
(3, [[1,2],[2,3]], -1)])
def test(n, trust, expected):
    actual = Solution().findJudge(n, trust)
    assert actual==expected