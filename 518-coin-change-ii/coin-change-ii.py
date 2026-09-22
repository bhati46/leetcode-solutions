class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp=[[-1]*(amount+1) for _ in range(len(coins))]
        def fun(target,i):
            if target==0:
                return 1
            if target < 0 or i == len(coins):
                return 0
            if dp[i][target]!=-1:
                return dp[i][target]
            take=fun(target-coins[i],i)
            nt=fun(target,i+1)
            dp[i][target]=(take+nt)
            return dp[i][target]
        return fun(amount,0)