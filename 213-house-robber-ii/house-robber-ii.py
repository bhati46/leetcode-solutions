class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def solve(arr):
            m=len(arr)
            dp=[-1]*(m+1)
            def fun(n):
                if n==0:
                    return 0
                if n==1:
                    return arr[0]
                if dp[n]!=-1:
                    return dp[n]
                t=arr[n-1]+fun(n-2)
                nt=fun(n-1)
                dp[n]=max(t,nt)
                return dp[n]
            return fun(m)
        return max(solve(nums[:-1]),solve(nums[1:]))