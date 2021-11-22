import pytest

from solution import can_attend_all_appointments

@pytest.mark.parametrize("input, expected", [
	( [[1,4], [2,5], [7,9]], False),
	([[6,7], [2,4], [8,12]], True),
	([[4,5], [2,3], [3,6]], False)
	])
def test(input, expected):
	actual = can_attend_all_appointments(input)
	assert actual == expected