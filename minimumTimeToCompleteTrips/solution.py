class Solution:
    def __count_trips(self, time, t) -> int:
        return sum([t // i for i in time])

    def __minimum_time(self, s, e, time, totalTrips) -> int:
        if s == e:
            return s
        m = s + (e - s) // 2
        trips = self.__count_trips(time, m)

        if trips >= totalTrips:
            return self.__minimum_time(s, m, time, totalTrips)
        else:
            return self.__minimum_time(m + 1, e, time, totalTrips)

    def minimumTime(self, time: list[int], totalTrips: int):
        return self.__minimum_time(0, time[-1] * totalTrips, time, totalTrips)


"""
9 3 10 5 total=2
3 5 9 10
t=3
trips = 3/3=3
t=(3)=
    i=0
    m=min(inf,2)

"""
