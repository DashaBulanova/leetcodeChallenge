import pytest

from contiguousArray.solution import Solution
from findMedianFromDataStream.solution import MedianFinder


def test():
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5
    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.0

def test_2():
    median_finder = MedianFinder()
    median_finder.addNum(6)
    assert median_finder.findMedian() == 6.0
    median_finder.addNum(10)
    assert median_finder.findMedian() == 8.0
    median_finder.addNum(2)
    assert median_finder.findMedian() == 6.0
    median_finder.addNum(6)
    assert median_finder.findMedian() == 6.0
    median_finder.addNum(5)
    assert median_finder.findMedian() == 6.0
    median_finder.addNum(0)
    assert median_finder.findMedian() == 5.5
    median_finder.addNum(6)
    assert median_finder.findMedian() == 6.0
    median_finder.addNum(3)
    assert median_finder.findMedian() == 5.5
    median_finder.addNum(1)
    assert median_finder.findMedian() == 5.0
    median_finder.addNum(0)
    assert median_finder.findMedian() == 4.0
    median_finder.addNum(0)
    assert median_finder.findMedian() == 3.0
