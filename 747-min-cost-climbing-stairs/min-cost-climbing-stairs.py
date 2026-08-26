class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp =[-1]*(n+1)
        def fun(i):
            if i>=n:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(fun(i+1),fun(i+2))
            return dp[i]
        return min(fun(0),fun(1))