import pytest

from core.utils.treeNodeConvert import to_binary_tree
from .solution import count_paths


@pytest.mark.parametrize("input, target, expected",
                         [
                             ([12, 7, 1, 4, 10, 5], 11, 2),
                             ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
                             ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3)
                         ])
def test(input, target, expected):
    root = to_binary_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    actual = count_paths(root, 8)
    assert actual == 3
