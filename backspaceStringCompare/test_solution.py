import pytest

from backspaceStringCompare.solution import Solution


@pytest.mark.parametrize("s, t, expected",
                          [
                             ('c', '#cb#', True),
                             ("ab#c", "ad#c", True),
                             ("a##c", "#a#c", True),
                             ("a#c", "b", False),
                             ("ab##", "c#d#", True),
                             ('#', '#cb#', False),
                             ("bbbextm", "bbb#extm", False),
                             ("bbb", "bb", False),
                             ("nzp#o#g", "b#nzp#o#g", True),
                         ])
def test_solution(s, t, expected):
    actual = Solution().backspaceCompare(s, t)
    assert actual == expected


@pytest.mark.parametrize("origin, current_index, expected",
                         [
                             ('abc#', 4, 1),
                             ('abc#', 1, 0),
                             ('a##', 3, -1),
                             ('a#b#h#', 6, -1),
                         ])
def test_get_significant_index(origin, current_index, expected):
    actual = Solution().get_next_significant_index(origin, current_index)
    assert actual == expected
