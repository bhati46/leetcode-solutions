from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        INF = 10**9

        # Step 1: Multi-source BFS
        dist = [[INF] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            x, y = q.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == INF:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        # Step 2: Max-Heap Dijkstra
        pq = [(-dist[0][0], 0, 0)]
        vis = [[False] * n for _ in range(n)]

        while pq:
            safe, x, y = heapq.heappop(pq)
            safe = -safe

            if vis[x][y]:
                continue

            vis[x][y] = True

            if x == n - 1 and y == n - 1:
                return safe

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny]:
                    heapq.heappush(
                        pq,
                        (-min(safe, dist[nx][ny]), nx, ny)
                    )

        return 0