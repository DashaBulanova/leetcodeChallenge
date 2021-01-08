def build_max_heap(unordered: []):
    n = int(len(unordered) / 2) - 1

    for i in range(n, -1, -1):
        max_heapify(unordered, i)


def left(index):
    return 2 * index + 1


def right(index):
    return 2 * index + 2


def parent(index):
    return int(index/2)


def insert(A: [], key: int):
    A.append(key)
    build_max_heap(A)


def swap(A, i, j):
    saved = A[i]
    A[i] = A[j]
    A[j] = saved


def max_heapify(A: [], i: int):
    left_index = left(i)
    right_index = right(i)

    largest = i
    if len(A) > left_index and A[largest] < A[left_index]:
        largest = left_index
    elif len(A) > right_index and A[largest] < A[right_index]:
        largest = right_index

    if largest != i:
        swap(A, i, largest)
        max_heapify(A, largest)