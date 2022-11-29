import pytest
from .solution import RandomizedSet


def test():
    rs = RandomizedSet()
    print(rs.insert(0))
    print(rs.insert(1))
    print(rs.remove(0))
    print(rs.insert(2))
    print(rs.remove(1))
    print(rs.getRandom())
