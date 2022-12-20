import collections


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        d = set([i for i in range(len(rooms))])
        q = collections.deque([0])

        while q:
            room = q.pop()
            if room in d:
                d.remove(room)
            keys = rooms[room]
            for key in keys:
                if key in d:
                    q.append(key)

        return len(d) == 0


"""
[1], [2], [3], []
q=0
d=0.1.2,3

room=0 q=[]
d=1.2.3
keys=1
q={1}

room=1
d=2,3
keys=[2]
q={2}

room=2
keys=3
d=3
q=3

room=3
d=[]



"""
