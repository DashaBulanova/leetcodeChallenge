__all__ = ['heapify', 'k_largest']


class Heap:

    def __init__(self, A: []):
        self._A = A

    @property
    def length(self):
        return len(self._A)

    @property
    def heap_size(self):
        return


def heapify(x: []):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)

    for i in reversed(range(n // 2)):
        _heapify(x, i)


def extract_max(x: []):
    max_element = x.pop(0)
    heapify(x)
    return max_element


# time-complexity O(klgn) => in a worst-case k=n O(nlgn)
def k_largest(heap: [], k: int) -> int:
    largest = 0
    for i in range(0, k):
        largest = extract_max(heap)
    return largest


def insert(x: [], key: int):
    x.append(key)
    heapify(x)


def _heapify(x: [], pos: int):
    largest = _get_largest(x, pos)

    if largest != pos:
        _swap(x, pos, largest)
        _heapify(x, largest)


def _swap(x: [], i: int, j: int):
    saved = x[i]
    x[i] = x[j]
    x[j] = saved


def _get_largest(x: [], parent: int):
    left = 2 * parent + 1
    right = 2 * parent + 2
    largest = parent
    if len(x) > left and x[parent] < x[left]:
        largest = left
    if len(x) > right and x[largest] < x[right]:
        largest = right

    return largest
