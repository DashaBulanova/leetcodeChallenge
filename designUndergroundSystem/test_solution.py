from designUndergroundSystem.solution import UndergroundSystem

def test_only_one_trip():
    sut = UndergroundSystem()
    sut.checkIn(45, "Leyton", 3)
    sut.checkOut(45, "Waterloo", 15)
    actual = sut.getAverageTime("Leyton", "Waterloo")
    assert actual is 12

