import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected", [
    ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
    ([[4, 3, 1], [3, 2, 4], [3], [4], []], [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]),
    ([[4, 3, 1], [3, 2, 4], [], [4], []], [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 4]])
])
def test(input, expected):
    actual = Solution().allPathsSourceTarget(input)
    assert actual == expected


"""
results=[]

getPath(0,acc)=>
    acc = [0]
    child=4
    acc=[0,4]
    getPaht(4, [0,4])=>
        results=[0,4]
    acc=[0]

    child=3
    acc=[0,3]
    getPath(3, [0,3])=>
        acc=[0,3,4]
        getPath(4,[0,3,4])

"""
