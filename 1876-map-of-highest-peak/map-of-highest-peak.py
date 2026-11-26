class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        dr = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        n = len(isWater)
        m = len(isWater[0])
        q = deque()
        visited = [[-1] * m for _ in range(n)]

        # image = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    q.append((i, j, 0))
                    visited[i][j] = 1
        while q:
            x, y, level = q.popleft()
            isWater[x][y] = level
            for k, l in dr:
                nx = x + k
                ny = y + l
                if nx>=n or ny>=m or nx<0 or ny<0:
                    continue
                if visited[nx][ny] == -1:
                    visited[nx][ny] = 1
                    q.append((nx, ny, level + 1))

        return isWater
