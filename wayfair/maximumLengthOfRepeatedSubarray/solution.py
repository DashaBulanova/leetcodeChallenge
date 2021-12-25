from typing import List

class Solution:
    def exists(self, subarray: List[int], nums2: List[int]) -> bool:
        win_lenght = len(subarray)
        start = 0
        end = win_lenght-1
        while end < len(nums2):
            if subarray == nums2[start:end+1]:
                return True
            else:
                end += 1
                start += 1

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        start, end = 0, 0
        while end<len(nums1):
            if self.exists(nums1[start:end+1], nums2):
                result = max(result, end+1 - start)
            else:
                start += 1
                while start<=end:
                    if self.exists(nums1[start:end+1], nums2):
                        result = max(result, end+1 - start)
                        break
                    start+=1
            end += 1
                

        return result
