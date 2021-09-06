import pytest

from .solution import Solution


@pytest.mark.parametrize("input, pattern, expected",
                         [
                             ("ppqp", "pq", [1, 2]),
                             ("abbcabc", "abc", [2, 3, 4]),
                         ])
def test_number_of_bits(input, pattern, expected):
    actual = Solution().find_string_anagrams(input, pattern)
    assert actual == expected
