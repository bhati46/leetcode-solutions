class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        dr=[[-1,0],[0,-1],[0,1],[1,0]]
        n=len(grid)
        m=len(grid[0])

        c=0

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    c+=4          # max boundaries a  grid[i][j]=4

                    for k,l in dr:
                        nx=k+i
                        ny=l+j
                        if nx>=n or ny>=m or nx<0 or ny<0:
                            continue
                        if grid[nx][ny]==1:
                            c-=1        # subtract -1 if it is connected another 1

        return c
