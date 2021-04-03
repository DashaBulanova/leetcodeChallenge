class UndergroundSystem:
    def __init__(self):
        self.check_in = dict()
        self.average = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName.lower(), t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time = self.check_in[id]
        key = f'{start_time[0]}_{stationName.lower()}'
        if key in self.average:
            self.average[key] = ((t - start_time[1]) + self.average[key][0], self.average[key][1] + 1)
        else:
            self.average[key] = (t - start_time[1], 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = f'{startStation.lower()}_{endStation.lower()}'
        return self.average[key][0]/self.average[key][1]