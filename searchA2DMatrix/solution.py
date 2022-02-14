from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rs,re=0,len(matrix)-1
        while rs<=re:
            rmid=rs+(re-rs)//2
            cs,ce=0, len(matrix[0])-1
            while cs<ce:
                cmid=cs+(ce-cs)//2
                if matrix[rmid][cmid]==target:
                    return True
                if target<matrix[rmid][cmid]:
                    ce = cmid
                else:
                    cs = cmid+1
            if matrix[rmid][cs]==target:
                return True
            if target<matrix[rmid][cs]:
                re=rmid-1
            else:
                rs=rmid+1
        return False