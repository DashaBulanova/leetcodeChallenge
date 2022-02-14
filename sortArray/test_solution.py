import pytest

from sortCharactersByFrequency.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [("tree", "eert"),
                         ("cccaaa", "aaaccc"),
                         ("Aabb", "bbaA")
                          ])
def test_number_of_bits(input, expected):
    actual = Solution().frequencySort(input)
    assert actual == expected
