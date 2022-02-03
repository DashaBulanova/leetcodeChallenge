import pytest

from .solution import Solution


@pytest.mark.parametrize("nums1, nums2, nums3, nums4, expected", [
    ([1, 2], [-2, -1], [-1, 2], [0, 2], 2),
    ([0],[0],[0],[0], 1),
    ([0,1,-1], [-1,1,0], [0,0,1],[-1,1,1], 17)
])
def test(nums1, nums2, nums3, nums4, expected):
    actual = Solution().fourSumCount(nums1, nums2, nums3, nums4)
    assert actual == expected

"""
nums1=[1, 2]
nums2=[-2, -1]
nums3=[-1, 2]
nums4=[0, 2]

result=0
1 => threeSum(nums2,nums3,nums4, -1) = >result = 1
    i=-2
    twoSum(nums3, nums4, -1 +2=1) => result = 1
        hashmap={-1, 2}

        j=0:
        1-0=1 in hashmap = False

        j=1:
        1-2=-1 in hashmap = True 
        result 1
        return 1
    i=-1
    twoSum(nums3, nums4, -1 +1 =0) => result = 0
        hashmap={-1, 2}

2 => threeSum(nums2,nums3,nums4, -2)
    i=-2
    twoSum(nums3, nums4, -2 +2=0)

    i=-1
    twoSum(nums3, nums4, -2 +1=-1)



"""

