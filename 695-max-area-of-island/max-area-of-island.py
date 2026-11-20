class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        n=len(grid[0])
        m=len(grid)

        if n==1 and m==1 and grid[0][0]==1:
            return 1

        dr=[[1,0],[0,1],[-1,0],[0,-1]]

        count=0

        visited=[[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if visited[i][j] == True:
                    continue
                if grid[i][j] == 0:
                    continue
            
                q=deque([(i,j)])
                visited[i][j]=True

                areamax=1

                while q:
                    x,y = q.popleft()
                    for k,l in dr:
                        nx=k+x
                        ny=l+y
                        if nx<0 or ny<0 or nx>=m or ny>=n:
                            continue
                        if visited[nx][ny] == True:
                            continue
                        if grid[nx][ny]== 0:
                            continue 
                        q.append((nx,ny))
                        visited[nx][ny] = True

                        areamax+=1
                count=max(count,areamax)
        return count

