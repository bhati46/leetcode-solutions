class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        x=[0]*(max(nums)+1)
        n=len(nums)
        dp=[-1]*(len(x)+1)
        for i in range(n):
            x[nums[i]]+=1
        def fun(i):
            if i>=len(x):
                return 0
            if dp[i] != -1:
                return dp[i]
            t = x[i]*i+fun(i+2)
            nt =fun(i+1)
            dp[i] = max(t,nt)
            return dp[i]
        return fun(0)