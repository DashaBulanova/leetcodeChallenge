import pytest

from .solution import Solution


@pytest.mark.parametrize("input, target, expected", [
    ([10, 5, 2, 6], 100, 8),
    ([1,2,3], 0, 0),
    ([10, 5, 2, 6], 5, 1)
])
def test(input, target, expected):
    actual = Solution().numSubarrayProductLessThanK(input, target)
    assert actual == expected


"""
[10, 5, 2, 6]
10 false
5 false
end=0
acc = 10
start=1




[10,5,2,6]
10 res=1 [10] + 1
10*5=50 res=3 [10 5] [5] +2
10*5*2=100 
5*2=10 res=5 [5 2] [2] + 2
5*2*6= res=8 [5 2 6] [2 6] [6] 3

[10,5,2,6]
end =0
acc=10
100<100:
    result = 1

edn=1
acc=50
    result=2-0=3

end=2
acc=100
while 100>=100:
    acc/=10=10
    start =1
result=3+(2+1-1)=5

end=3
acc=60
result=5+(3+1-1)=8

"""
