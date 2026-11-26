class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        dr = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        n = len(grid)
        m = len(grid[0])
        q = deque()
        visited = [[-1] * m for _ in range(n)]

        image = [[-1] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
                    visited[i][j] = 1
        while q:
            x, y, level = q.popleft()
            image[x][y] = level
            for k, l in dr:
                nx = x + k
                ny = y + l
                if nx>=n or ny>=m or nx<0 or ny<0:
                    continue
                if visited[nx][ny] == -1:
                    visited[nx][ny] = 1
                    q.append((nx, ny, level + 1))
        maxi=0
        for i in range(n):
            for j in range(m):
                maxi=max(maxi,image[i][j])
        return maxi if maxi>0 else -1
