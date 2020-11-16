import pytest

from cheapestFlightsWithinKStops.solution import Solution


@pytest.mark.parametrize("n, edges, src, dst, k, expected",
                         [(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200)]
                         )
def test_number_of_bits(n, edges, src, dst, k, expected):
    actual = Solution().findCheapestPrice(n, edges, src, dst, k)
    assert actual == expected
