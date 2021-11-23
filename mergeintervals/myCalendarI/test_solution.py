from solution import MyCalendar


def test():
    calendar = MyCalendar()

    assert calendar.book(20, 29)
    assert not calendar.book(13, 22)
    assert calendar.book(44, 50)
    assert calendar.book(1, 7)
    assert not calendar.book(2, 10)
    assert not calendar.book(21, 29)

    # assert calendar.book(20, 30)
"""
["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
[[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]

[null,true,true,false,false,true,false,false,true,true,false]
[null,true,true,false,false,true,false,true,true,true,false]

[25,32] [19,25]

event[0]=25 event[1]=32 start=19 end=25

32<=19 false 
"""
