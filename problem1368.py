import heapq

class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        
        directions = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }

        pq = [(0, 0, 0)]
        visited = [[False] * n for _ in range(m)]
        
        while pq:
            cost, i, j = heapq.heappop(pq)
            
            if i == m - 1 and j == n - 1:
                return cost
            
            if visited[i][j]:
                continue
            visited[i][j] = True
            
            for direction, (di, dj) in directions.items():
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    new_cost = cost if grid[i][j] == direction else cost + 1
                    if not visited[ni][nj]:
                        heapq.heappush(pq, (new_cost, ni, nj))

        return -1 