import pytest

from core.utils.treeNodeConvert import to_binary_tree
from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [([1, 2, 3], 25),
                          ([4,9,0,5,1], 1026)
                          ])
def test(input, expected):
    tree = to_binary_tree(input)
    actual = Solution().sumNumbers(tree)
    assert actual == expected
