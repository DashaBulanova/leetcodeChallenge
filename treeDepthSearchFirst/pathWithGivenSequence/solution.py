# Definition for a binary tree node.
from typing import List

from core.dataStructure.TreeNode import TreeNode


def _is_leaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None


def find_path_recursive(node: TreeNode, sequence: List[int], index: int):
    if node is None:
        return False

    if index >= len(sequence):
        return False

    if node.val != sequence[index]:
        return False

    if _is_leaf(node) and index == len(sequence) - 1:
        return True

    return find_path_recursive(node.left, sequence, index + 1) or find_path_recursive(node.right, sequence, index + 1)


def find_path(root: TreeNode, sequence):
    if len(sequence) == 0:
        return False
    return find_path_recursive(root, sequence, 0)
