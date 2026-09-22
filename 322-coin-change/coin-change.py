class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp=[[-1]*(amount+1)for _ in range(len(coins))]
        def fun(dp,target,i):
            if target==0:
                return 0
            if i==len(coins) or target < 0:
                return float('inf')
            if dp[i][target]!=-1:
                return dp[i][target]
            take=1+fun(dp,target-coins[i],i)
            nt=fun(dp,target,i+1)
            dp[i][target]=min(take,nt)
            return dp[i][target]
        ans=fun(dp,amount,0)
        return ans if ans!=float('inf') else -1