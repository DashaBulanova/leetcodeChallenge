import pytest

from .solution import backspace_compare


@pytest.mark.parametrize("str1, str2, expected",
                         [
                             ("xy#z", "xzz#", True),
                             ("xy#z", "xyz#", False),
                             ("xp#", "xyz##", True),
                             ("xywrrmp", "xywrrmu#p", True),
                             ("ab##", "c#d#", True),
                             ("a##c", "#a#c", True),
                             ("bxj##tw", "bxo#j##tw", True),
                             ("bxj##tw", "bxj###tw", False),
                         ])
def test(str1, str2, expected):
    actual = backspace_compare(str1, str2)
    assert actual == expected
