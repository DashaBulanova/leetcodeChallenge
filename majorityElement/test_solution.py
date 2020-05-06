import pytest

from majorityElement.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [([3, 2, 3], 3),
                          ([2, 2, 1, 1, 1, 2, 2], 2)
                          ])
def test_number_of_bits(input, expected):
    actual = Solution().majorityElement(input)
    assert actual == expected
