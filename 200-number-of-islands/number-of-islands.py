class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)


        n = len(grid[0])

        dr = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        visited = [[False] * n for _ in range(m)]

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                if visited[i][j] == True:
                    continue

                count += 1

                q = deque([(i, j)])
                visited[i][j] = True

                while q:
                    x, y = q.popleft()
                    for k, l in dr:
                        nx = k + x
                        ny = l + y
                        if nx < 0 or ny < 0 or nx >= m or ny >= n:
                            continue
                        if visited[nx][ny] == True:
                            continue
                        if grid[nx][ny] == "0":
                            continue
                        q.append((nx, ny))
                        visited[nx][ny] = True
        return count