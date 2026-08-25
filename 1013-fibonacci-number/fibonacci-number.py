class Solution:
    def fib(self, n: int) -> int:
        dp=[-1]*(n+1)
        def memo(n,dp):
            if n==0 or n==1:
                return n
            if dp[n]!=-1:
                return dp[n]
            dp[n]=memo(n-1,dp)+memo(n-2,dp)
            return dp[n]
        return memo(n,dp)