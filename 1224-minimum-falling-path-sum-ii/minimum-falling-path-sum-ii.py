class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        a=float('inf')
        dp=[[0]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0:
                    dp[i][j]=grid[i][j]
                    continue
                y=float('inf')
                for k in range(len(grid)):
                    if k==j:
                        continue
                    y=min(dp[i-1][k],y)
                dp[i][j]=y+grid[i][j]
        return min(dp[len(grid)-1])