class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(_in_order_traversal_iter(self))


def _in_order_traversal_iter(node: TreeNode) -> []:
    current = node
    stack = []
    result = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            result.append(current.val)
            current = current.right
        else:
            break
    return result


def _in_order_traversal(node: TreeNode, result: []) -> []:
    if node is None:
        return result
    else:
        _in_order_traversal(node.left, result)
        result.append(node.val)
        _in_order_traversal(node.right, result)
    return result


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(5)
    tree.right.right = TreeNode(7)

    print(str(tree))
