from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        fresh = 0
        minutes = 0

        # Step 1: Count fresh & add rotten to queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        # Step 2: BFS until no fresh left
        while q and fresh > 0:
            minutes += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        q.append((ni, nj))
                        fresh -= 1

        # Step 3: Check if all fresh are rotten
        return -1 if fresh > 0 else minutes
