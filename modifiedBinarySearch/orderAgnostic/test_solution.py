"""
input = [4, 6, 10], key = 10

search(input, 10, 0, 2)
mid = 0+(2-0/2)=1

left = search(input, 10, 0, 1) -> - 1
    mid=0+(1-0)/2=0
    left = search(input, 10, 0, 0) -> -1
        return -1
    right = search(input, 10, 1, 1) ->
        return -1
right = search(2,2) -> 2
return 2

"""
import pytest
from solution import search_key

@pytest.mark.parametrize("input, target, expected", [
        ([4, 6, 10], 10, 2),
        ([10, 6, 4], 10, 0),
        ([1, 2, 3, 4, 5, 6, 7], 5, 4),
        ([10, 6, 4], 4, 2),
    ])
def test(input, target, expected):
    actual = search_key(input, target)
    assert actual == expected
