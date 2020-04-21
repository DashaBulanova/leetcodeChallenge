import pytest

from productOfArrayExceptSelf.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([1, 2, 3, 4], [24, 12, 8, 6]),
                             ([1,0], [0,1])
                         ])
def test_number_of_bits(input, expected):
    actual = Solution().productExceptSelf(input)
    print(type(expected))
    assert actual == expected
