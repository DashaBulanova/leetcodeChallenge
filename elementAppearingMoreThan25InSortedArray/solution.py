class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        count = 25*len(arr)/100
        d = {}
        for i in range(len(arr)):
            d[arr[i]] = d.get(arr[i], 0) + 1
            print(f'{i}:{d[arr[i]]}')
            if d[arr[i]]>count:
                return arr[i]
                       
        raise ValueError()
        
