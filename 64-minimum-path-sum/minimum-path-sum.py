class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        INF = float('inf')
        dp =[[0]* len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    dp[0][0]=grid[0][0]
                    continue
                if i-1<0:
                    up=INF
                else:
                    up=dp[i-1][j]
                if j-1<0:
                    left=INF
                else:
                    left=dp[i][j-1]
                dp[i][j]=grid[i][j]+min(up,left)
        return dp[len(grid)-1][len(grid[0])-1]