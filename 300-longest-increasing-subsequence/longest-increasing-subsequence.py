class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[[-1]*(n+1) for _ in range(n+1)]
        def fun(i,p):
            if i>=n:
                return 0
            if dp[i][p]!=-1:
                return dp[i][p]
            t=0
            if p==-1 or nums[i]>nums[p]:
                t=1+fun(i+1,p=i)
            nt=fun(i+1,p)
            dp[i][p]=max(nt,t)
            return dp[i][p]
        return fun(0,-1)