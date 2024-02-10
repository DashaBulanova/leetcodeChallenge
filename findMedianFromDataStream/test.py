from .solution import MedianFinder

def test():
    finder = MedianFinder()
    finder.addNum(22)
    assert finder.findMedian() == 22

    finder.addNum(35)
    assert finder.findMedian() == (22+35)/2

    finder.addNum(30)
    assert finder.findMedian() == 30

    finder.addNum(25)
    assert finder.findMedian() == (25 + 30) / 2

    finder.addNum(54)
    assert finder.findMedian() == 30

    finder.addNum(28)
    assert finder.findMedian() == (28 + 30) / 2

    finder.addNum(33)
    assert finder.findMedian() == 30

    finder.addNum(67)
    assert finder.findMedian() == (30 + 33) / 2

def test_1():
    [[], [-1], [], [-2], [], [-3], [], [-4], [], [-5], []]
    finder = MedianFinder()
    finder.addNum(-1)
    assert finder.findMedian() == -1

    finder.addNum(-2)
    assert finder.findMedian() == -1.5

    finder.addNum(-3)
    assert finder.findMedian() == -2

    finder.addNum(-4)
    assert finder.findMedian() == -2.5

    finder.addNum(-5)
    assert finder.findMedian() == -3
