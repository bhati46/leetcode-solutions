class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        m=len(dungeon)
        n=len(dungeon[0])
        dp=[[-1]*n for _ in range(m)]
        maxi=float('inf')
        def fun(i,j):
            if i>=m or j>=n:
                return maxi
            if i==m-1 and j==n-1:
                return max(1,1-dungeon[i][j])
            if dp[i][j]!=-1:
                return dp[i][j]
            down = fun(i+1,j)
            right = fun(i,j+1)
            dp[i][j]=max(1,min(right,down)-dungeon[i][j])
            return dp[i][j]
        return fun(0,0)