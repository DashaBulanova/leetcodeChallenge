__all__ = ['heapify', 'push', 'pop']


def heapify(x: []):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)

    for i in reversed(range(n//2)):
        _heapify(x, i)


def pop(x: []):
    min_element = x.pop(0)
    heapify(x)
    return min_element


def push(x: [], key: int):
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
    elif len(x) > right and x[smallest] > x[right]:
        smallest = right

    return smallest


class MinHeap:
    _heap = []

    def pop(self):
        min_element = self._heap.pop(0)
        heapify(self._heap)
        return min_element



    def _heap_size(self):
        return len(self._heap)

    def _swap(self, i, j):
        saved = self._heap[i]
        self._heap[i] = self._heap[j]
        self._heap[j] = saved

    @staticmethod
    def _left(index: int):
        return 2 * index + 1

    @staticmethod
    def _right(index):
        return 2 * index + 2

    @staticmethod
    def _parent(index):
        return int(index/2)

    def _push_down(self, pos: int):
        smallest = self._get_smallest(pos)

        if smallest != pos:
            self._swap(pos, smallest)
            self._push_down(smallest)

    def _get_smallest(self, parent: int):
        left = self._left(parent)
        right = self._right(parent)
        smallest = parent
        if self._heap_size() > left and self._heap[parent] > self._heap[left]:
            smallest = left
        elif self._heap_size() > right and self._heap[smallest] > self._heap[right]:
            smallest = right

        return smallest

    def _heapify(self):
        """Transform list into a heap, in-place, in O(len(x)) time."""
        n = self._heap_size()

        for i in reversed(range(n // 2)):
            self._push_down(i)




