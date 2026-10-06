class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def solve(arr):
            # we took m for arr because we have taken 1 less no. as we arwe conveting it to house robber 1
            m=len(arr)
            dp=[-1]*(m+1) # so we have take dp according to the new array
            # the function is same as the house robber one
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
        # we are passing two array in first we reversed array  and in second we remove the last house
        # case 1--> we are excluding the last house
        # case 2--> we are excluding the first house
        return max(solve(nums[:-1]),solve(nums[1:]))