__all__ = ['heapify', 'k_smallest', 'extract_min', 'insert']


def heapify(x: []):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)

    for i in reversed(range(n//2)):
        _heapify(x, i)


# time-complexity O(klgn) => in a worst-case k=n O(nlgn)
def k_smallest(heap: [], k: int) -> int:
    smallest = 0
    for i in range(0, k):
        smallest = extract_min(heap)
    return smallest


def extract_min(x: []):
    min_element = x.pop(0)
    heapify(x)
    return min_element


def insert(x: [], key: int):
    x.append(key)
    heapify(x)


def _heapify(x: [], pos: int):
    smallest = _get_smallest(x, pos)

    if smallest != pos:
        _swap(x, pos, smallest)
        _heapify(x, smallest)


def _swap(x: [], i: int, j: int):
    saved = x[i]
    x[i] = x[j]
    x[j] = saved


def _get_smallest(x: [], parent: int):
    left = 2 * parent + 1
    right = 2 * parent + 2
    smallest = parent
    if len(x) > left and x[parent] > x[left]:
        smallest = left
    if len(x) > right and x[smallest] > x[right]:
        smallest = right

    return smallest




