from constructBSTfromPreorderTraversal.solution import Solution

def to_breadth_traversal_format(treeNode):
    """

    :type treeNode: TreeNode
    """
    result = []
    append(treeNode, result)
    return result

def append(node, result):
    if node is None:
        result.append(None)
    else:
        result.append(node.val)
        append(node._left, result)
        append(node._right, result)

def test_bst_from_preorder():
    preorder = [8, 5, 1, 7, 10, 12]
    actual = Solution().bstFromPreorder(preorder)
    expected = [8,5,10,1,7,None,12]
    assert
