class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    if root is None:
        return sum == 0

    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)
#time compexity: O(N), N - nodes counts
#space complexity: O(N), we need this space for store recursion execution stack
