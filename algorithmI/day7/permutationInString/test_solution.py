import pytest

from .solution import Solution


@pytest.mark.parametrize("s1, s2, expected",
                         [
                             ("ab", "eidbaooo", True),
                             ("ab", "eidboabo", True),
                             ("ab", "eidboaoo", False),
                             ("ab", "a", False),
                             ("aa", "aa", True),
                             ("adc", "dcda", True),
                             ("hello", "ooolleoooleh", False),
                         ])
def test_number_of_bits(s1, s2, expected):
    actual = Solution().checkInclusion(s1, s2)
    assert actual == expected


"""
ooolleoooleh

h:1 e:1 l:2 0:1
t=5

s=0 e=0
s2[0]=o
h:1 e:1 l:2 0:0
t=4

s=0 e=1
s2[1]=o
h:1 e:1 l:2 0:0
t=4

s=0 e=2
s2[2]=d


"""