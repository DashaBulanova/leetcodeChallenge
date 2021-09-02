from .solution import NumArray


def test():
    sut = NumArray([-2, 0, 3, -5, 2, -1])
    assert sut.sumRange(0, 2) == 1
    assert sut.sumRange(2, 5) == -1
    assert sut.sumRange(0, 5) == -3
