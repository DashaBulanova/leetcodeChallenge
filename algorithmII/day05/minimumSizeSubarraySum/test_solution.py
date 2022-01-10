import pytest
from .solution import Solution

@pytest.mark.parametrize("input, target, expected", [
    ([2,3,1,2,4,3], 7, 2),
    ([8], 7, 1),
])
def test(input, target, expected):
    actual = Solution().minSubArrayLen(target, input)
    assert actual == expected

"""
[2,3,1,2,4,3]
2+3=5> false
2+3+1=6 false
2+3+1+2=8=true 4
3+1+2=6 false
3+1+2+4=10 true 4
1+2+4=7 = true 3
2+4+3 = true 3
4+3=true 2

s=0, e=0
result = 0
acc = 0


end=0
acc = 2
while 2>=7 false

end = 1
acc = 5
while 2>=7 false

end=2
acc=6
while 2>=7 false 

end=3
acc=8
while 8>=7 true 
    result = 3+1=4
    start = 1
    acc = 8-2=6

end=4
acc=10
while acc>=7 true
    result=4
    start=2
    acc=7
    
    result=3
    acc=6
    start=3

end=5
acc=9
while acc>=7:
    result=3
    acc=7
    start=4



"""