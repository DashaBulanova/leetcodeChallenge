from queue import Queue
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue = Queue()
        queue.put((sr, sc))
        starting_pixel = image[sr][sc]
        if starting_pixel == newColor:
            return image
        while not queue.empty():
            i, j = queue.get()
            image[i][j] = newColor
            if i + 1 < len(image) and image[i + 1][j] == starting_pixel:
                queue.put((i + 1, j))
            if i - 1 >= 0 and image[i - 1][j] == starting_pixel:
                queue.put((i - 1, j))
            if j + 1 < len(image[i]) and image[i][j + 1] == starting_pixel:
                queue.put((i, j + 1))
            if j - 1 >= 0 and image[i][j - 1] == starting_pixel:
                queue.put((i, j - 1))
        return image
