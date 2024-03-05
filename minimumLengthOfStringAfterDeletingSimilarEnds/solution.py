class Solution:
    def minimumLength(self, original: str) -> int:
        if len(original)<=1:
            return len(original)

        s,e=0,len(original)-1

        while original[s]==original[e] and s<e:
            char = original[s]
            while original[s] == char and s<e:
                s+=1
            while original[e] == char and e>=s:
                e-=1

        return e-s+1

"""
aabccabba
s,e=0,8

char=a
    s=2
    e=7
char=b
    s=3
    e=5


"""