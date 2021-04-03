from core.dataStructure.src.avl_tree import BST


def test_insert():
    bst = BST()
    bst.insert(41)
    bst.insert(20)
    bst.insert(29)
    bst.insert(26)
    bst.insert(11)
    bst.insert(65)
    actual = bst.insert(50)
    print(bst)
