class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[-1]* len(grid[0]) for i in range(len(grid))]
        def fun(i,j):
            if i==0 and j==0:
                return grid[0][0]
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if i-1<0:
                up=float('inf')
            else:
                up=grid[i][j]+fun(i-1,j)
            if j-1<0:
                left=float('inf')
            else:
                left=grid[i][j]+fun(i,j-1)
            dp[i][j]=min(up,left)
            return dp[i][j]
        return fun(len(grid)-1,len(grid[0])-1)