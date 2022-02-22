from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        q = deque([(0, 0)])
        grid[0][0] = 1
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        while q:
            i, j = q.popleft()

            dist = grid[i][j]
            if i == n - 1 and j == n - 1:
                return dist

            for di, dj in directions:
                if di+i < 0 or di+i > n - 1:
                    continue
                if dj+j < 0 or dj+j > n - 1:
                    continue
                if grid[di+i][dj+j] == 1:
                    continue

                if grid[di+i][dj+j] > 1:
                    continue

                grid[di+i][dj+j] = dist + 1
                q.append((di+i, dj+j))

        return -1
