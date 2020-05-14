import pytest

from happyNumber.solution import Solution
from implementPrefixTree.solution import Trie


# @pytest.mark.parametrize("input, expected",
#                          [(19, True),
#                          (17, False)])
def test_number_of_bits():
    obj = Trie()
    obj.insert('app')
    obj.insert('apps')
    actual = obj.search('app')
    assert actual is True


def test_number_of_bits1():
    obj = Trie()
    obj.insert('apple')
    actual = obj.search('app')
    assert actual is False


def test_start_with_if_exists():
    obj = Trie()
    obj.insert('apple')
    actual = obj.startsWith('app')
    assert actual is True


def test_start_with_if_not_exists():
    obj = Trie()
    obj.insert('apple')
    actual = obj.startsWith('apl')
    assert actual is False

