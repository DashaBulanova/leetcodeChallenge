import itertools

"""
oidbcaf
abc

window1: oid
for start to end:
    if str[window1] not in map:
        start ++
        
window2:idb
window3:dbc
window4:bca
 if str[window1] not in map:
        start ++
else: 
    map[str[window]]-1
    
if len(map) == 0 return True
window4:caf

"""

class Solution:
    def find_permutation(self, str, pattern):
        map = dict()
        for p in pattern:
            if p in map:
                map[p] += 1
            else:
                map[p] = 1

        window_start = 0

        temp = map.copy()  #don't like clone
        need_clone = False

        while window_start < len(str):
            if str[window_start] in temp:
                temp[str[window_start]] -= 1
                if temp[str[window_start]] == 0:
                    temp.pop(str[window_start])
                need_clone = True
            else:
                if need_clone:
                    temp = map.copy()
                    need_clone = False
            if len(temp) == 0:
                return True
            window_start += 1

        return False
