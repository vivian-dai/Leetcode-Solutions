class UndergroundSystem:

    def __init__(self):
        self.times = {}
        self.checked_in = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        t_start = self.checked_in[id][1]
        name = self.checked_in[id][0]
        if f"{name} {stationName}" in self.times:
            self.times[f"{name} {stationName}"].append(t - t_start)
        else:
            self.times[f"{name} {stationName}"] = []
            self.times[f"{name} {stationName}"].append(t - t_start)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total = 0
        for i in range(len(self.times[f"{startStation} {endStation}"])):
            total += self.times[f"{startStation} {endStation}"][i]
        return total/len(self.times[f"{startStation} {endStation}"])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
