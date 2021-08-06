from core.dataStructure.naryTree import Node
from .solution import Solution


def test_number_of_bits():
    root = Node(val=1)
    root.children = [Node(val=3, children=[Node(val=5), Node(val=6)]), Node(val=2), Node(val=4)]

    actual = Solution().levelOrder(root)
    assert actual == [[1], [3, 2, 4], [5, 6]]
