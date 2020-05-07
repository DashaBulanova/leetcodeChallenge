from core.dataStructure.TreeNode import TreeNode


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        cache = dict()
        self.fill_cache(root, None, 0, cache)
        return cache[x][0] == cache[y][0] and cache[x][1] != cache[y][1]

    def fill_cache(self, node: TreeNode, parent_val: int, depth: int, cache: dict):
        if node is None:
            return

        cache[node.val] = (depth, parent_val)
        self.fill_cache(node.left, node.val, depth + 1, cache)
        self.fill_cache(node.right, node.val, depth + 1, cache)
