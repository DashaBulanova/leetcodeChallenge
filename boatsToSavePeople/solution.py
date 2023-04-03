class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        if len(people) == 0:
            return 0

        people.sort()
        boats = 0
        s, e = 0, len(people)-1
        while s<=e:
            if s==e:
                boats+=1
                s+=1
            elif people[e] == limit:
                boats += 1
                e-=1
            elif people[e]+people[s]<=limit:
                boats+=1
                s+=1
                e-=1
            else:
                boats+=1
                e-=1
        return boats
"""
1,2 3
s=0 e=1
boats=1
s=1 e=0
"""
