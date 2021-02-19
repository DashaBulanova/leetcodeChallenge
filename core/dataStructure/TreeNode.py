from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(_in_order_traversal_iter(self))


def to_bst(input: []) -> TreeNode:
    r = []
    root = TreeNode(input.pop(0))
    r.append(root)

    while len(input) > 0:
        current = r.pop(0)
        item = input.pop(0)
        if item is not None:
            current.left = TreeNode(item)
            r.append(current.left)
        if len(input) > 0:
            item = input.pop(0)
            if item is not None:
                current.right = TreeNode(item)
                r.append(current.right)
        else:
            break

    return root


def to_array(root: TreeNode) -> []:
    return breadth_first_traversal(root)


def breadth_first_traversal(root: TreeNode) -> []:
    result = []
    queue = Queue()
    queue.put(root)
    count = 1
    while not queue.empty() and count > 0:
        node = queue.get()
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            count -= 1
            if node.left is not None:
                queue.put(node.left)
                count += 1
            else:
                queue.put(None)
            if node.right is not None:
                queue.put(node.right)
                count += 1
            else:
                queue.put(None)
    return result


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
