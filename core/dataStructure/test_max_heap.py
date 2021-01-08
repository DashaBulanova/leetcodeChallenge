from core.dataStructure.max_heap import insert


def test_insert():
    A = []
    insert(A, 1)
    insert(A, 4)
    insert(A, 6)
    insert(A, 2)
    insert(A, 9)
    insert(A, 3)
    expected = [9, 6, 4, 1, 2, 3]
    assert A == expected