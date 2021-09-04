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
        matched = 0

        for window_end in range(len(str)):
            if str[window_end] in map:
                map[str[window_end]] -= 1
                matched += 1

            if matched == len(pattern):
                return True

            if window_end-window_start+1 >= len(pattern):
                if str[window_start] in map:
                    map[str[window_start]] += 1
                    matched -= 1
                window_start += 1

        return False
