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



"""
s index always shows matched first index of needle s
    sadbutsad sad 
s   |         |
e   |

    sadbutsad sad 
s   |          |
e    |

    sadbutsad sad 
s   |           |
e     |
sad sad

aaaba aaba

"""