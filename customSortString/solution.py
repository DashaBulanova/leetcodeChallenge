# class OrderedSet:

#     def __init__(order: str):
#         self.dict = {}
#         for c in order:
#             self.dict[c] = self.dict.get(c,0)+1
#         self.len = len(self.dict)

#     def __iter__(self):
#         self.dict.__iter__()
        

#     def __next__(self):
#         if self.n <= self.len:
#             self.dict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {} # k:v => char = order index
        for i in range(len(order)): #O(1)
            d[order[i]] = i

        outbox=27
        result = {} #k:v => order_index: (char, frequency)
        for i in range(len(s)): #O(m=len(s))
            char = s[i]
            if char in d: #O(1)
                if d[char] in result:
                    result[d[char]]=(char, result[d[char]][1]+1)
                else:
                    result[d[char]]=(char, 1)
            else:
                result[outbox]=(char,1)
                outbox+=1

        s = ""
        for k in sorted(result.keys()):
            s += result[k][0]*result[k][1]

        return s