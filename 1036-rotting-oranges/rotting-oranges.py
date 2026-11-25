class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        fresh=0

        q=deque()

        dr=[[-1,0],[0,-1],[0,1],[1,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1

        visited=[[False]*m for _ in range(n)]

        minutes=0
        
        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for k, l in dr:
                    nx = x + k
                    ny = y + l
                    if nx >= n or ny >= m or nx < 0 or ny < 0:
                        continue
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))

            minutes += 1
        return minutes if fresh == 0 else -1