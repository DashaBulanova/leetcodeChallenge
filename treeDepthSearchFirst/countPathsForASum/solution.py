# Definition for a binary tree node.
from typing import List

from core.dataStructure.TreeNode import TreeNode


def count_paths_recursive(node: TreeNode, target: int, path_acc: List[int]) ->int:
    if not node:
        return 0

    path_acc.append(node.val)

    result = 0
    agg_sum = 0
    for i in range(len(path_acc)-1, -1, -1):
        agg_sum += path_acc[i]
        if agg_sum == target:
            result += 1

    result += count_paths_recursive(node.left, target, path_acc) + count_paths_recursive(node.right, target, path_acc)
    del path_acc[-1]
    return result


def count_paths(root, S):
  return count_paths_recursive(root, S, [])