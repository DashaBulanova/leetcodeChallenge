from typing import List
from operator import itemgetter


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        real_index = []
        reconstructed_queue = []

        for i in range(0, len(people)):
            real_index.append(i)
            reconstructed_queue.append(0)

        people = sorted(sorted(people, key=itemgetter(1), reverse=True), key=itemgetter(0))

        for person in people:
            reconstructed_queue[real_index[person[1]]] = person
            del real_index[person[1]]

        return reconstructed_queue
