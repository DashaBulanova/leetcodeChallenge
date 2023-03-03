class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s, e = 0, len(needle)

        while e<=len(haystack):
            if haystack[s:e] == needle:
                return s
            else:
                s+=1
                e+=1
        
        return -1
#k=len(needle)
#n=len(heystack)
#O(nk)



"""
s index always shows matched first index of needle s
    sadbutsad sad 
     |         |
       |

    sadbutsad sad 
s   |          |
e    |

    sadbutsad sad 
s   |           |
e     |
sad sad

aaaba aaba

"""