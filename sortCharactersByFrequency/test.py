import pytest
from .solution import Solution

@pytest.mark.parametrize("input, expected", [
("tree", "eetr"),
("cccaaa", "cccaaa"),
("Aabb", "bbAa")
])
def test(input, expected):
	actual = Solution().frequencySort(input)
	assert actual == expected
