from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def paths(node: TreeNode, target: int, current_path: List[int], result: List[List[int]]):
    if node is None:
        return

    current_path.append(node.val)

    if target - node.val == 0 and node.right is None and node.left is None:
        result.append(list(current_path))
    else:
        paths(node.left, target - node.val, current_path, result)
        paths(node.right, target - node.val, current_path, result)

    del current_path[-1]


def find_paths(root: TreeNode, sum: int) -> List[List[int]]:
    allPaths = []

    paths(root, sum, [], allPaths)
    return allPaths

# time compexity: O(N), N - nodes counts
# space complexity: O(2N), we need this space for store recursion execution stack
