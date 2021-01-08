from core.dataStructure.min_heap import heapify, push, pop


def test_min_heap():
    input = [1, 4, 6, 2, 9, 3]
    expected = [1, 2, 3, 4, 9, 6]
    heapify(input)
    assert input == expected


def test_push():
    A = []
    push(A, 2)
    push(A, 9)
    push(A, 7)
    push(A, 12)
    push(A, 11)
    push(A, 10)
    push(A, 8)
    expected = [2, 9, 7, 12, 11, 10, 8]
    assert A == expected


def test_pop():
    A = [2, 9, 7, 12, 11, 10, 8]
    actual = pop(A)
    assert actual == 2
    actual = pop(A)
    assert actual == 7
    actual = pop(A)
    assert actual == 8
