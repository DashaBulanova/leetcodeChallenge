from core.dataStructure.min_heap import push


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        ugly_numbers = []

        prime_factors = [2, 3, 5]
        min_heap1, min_heap2, min_heap3 = []

        self._build_heap(min_heap1, 2, [3, 4])

        s = 'test'

    def _build_heap(self, heap: [], root: int, multipliers: []):
        queue = [], new_level = []
        push(heap, root)
        queue.append(root)
        for level in range(0, 10):
            while len(queue) > 0 and len(queue):
                current = queue.pop()
                for multiplier in multipliers:
                    value = current * multiplier
                    push(heap, value)
                    new_level.append(value)
            queue = new_level
