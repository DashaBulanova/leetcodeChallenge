import pytest
from .solution import RandomizedSet


def test():
    rs = RandomizedSet()
    print(rs.insert(53))
    print(rs.insert(12))
    print(rs.remove(53))
    print(rs.insert(23))
    print(rs.remove(12))
    print(rs.getRandom())
