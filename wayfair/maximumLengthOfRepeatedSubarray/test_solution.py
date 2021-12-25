"""
nums1=[1,2,3,2,1] nums2=[3,2,1,4,7]

start = 0
end = 0
    exists(nums[1], nums2)=>
        len = 1
        start = 0
        end =0
            [1] == [3] False
            end = 1
            start =1

            [1] == [2] False
            end=2, start =2

            [1] == [1] True
    result = 1
    end = 1

    exists([1,2], nums2) => false
        len =2
        start, end = 0, 1
        1<5 True
            [1,2] == [3,2] False
            start=1
            end=2

            [1,2] == [2, 1] False
            start =2 end =3

            [1,2] == [1,4] False
            start = 3 end=4

            [1,2] == [4,7] False
            start = 4 end=5
     else:
        start =1
        1<=1:
            exists([2]) => True
            result = 1
        end=2

    exists=[2,3]=False
        start=2
        exists([3]) True
        result =1
    end=3
    
    exists[3,2]=True
        result = 2
    end=4
    4<5
    exists[3,2,1]=True
        result=3



"""


import pytest
from .solution import Solution

@pytest.mark.parametrize("nums1, nums2, expected",[
    ([1,2,3,2,1], [3,2,1,4,7], 3),
    ([0,0,0,0,0], [0,0,0,0,0], 5)
    ])
def test(nums1, nums2, expected):
    actual = Solution().findLength(nums1, nums2)
    assert actual == expected