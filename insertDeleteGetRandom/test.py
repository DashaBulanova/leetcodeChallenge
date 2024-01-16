import pytest
from .solution import RandomizedSet

def test():
    sut = RandomizedSet()
    sut.insert(1)
    sut.remove(2)
    sut.insert(2)
    sut.getRandom()
    sut.remove(1)
    sut.insert(2)
