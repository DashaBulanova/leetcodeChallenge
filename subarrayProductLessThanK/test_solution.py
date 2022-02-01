import pytest
from .solution import Solution

@pytest.mark.parametrize("input, target, expected", [
([10,5,2,6], 100, 8),
([1,2,3], 0, 0),
([1,2,3], 1, 0),
    ])
def test(input, target, expected):
    actual = Solution().numSubarrayProductLessThanK(input, target)
    assert actual == expected

"""
[1,2,3] target=1
acc=1
end=0 start=0
acc /= 1
start=1

result = 0-1+1=0
end=1

acc = 2
acc=1
start =2




[10,5,2,6] target=100

start=0
acc=1
result=0

end=0
acc = arr[0]=10
result = 0-0+1=1

end=1
acc = arr[1]=10*5=50
result =1-0+1=3

end=2
acc=50*2=100
while 100>=100:
    acc/= arr[0] /=10=10
    start=1
result = 3+2-1+1=5

end=3
acc=10*6=60
result=5+3-1+1=8


"""
