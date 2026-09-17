class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        n=len(nums)
        total=sum(nums)
        target=total//2
        dp = [[-1 for _ in range(total+2)] for _ in range(n)]
        if total%2!=0:
            return False
        def fun(i,curr):
            if curr == 0:
                return True
            if i == n or curr < 0:
                return False
            if dp[i][curr]!=-1:
                return dp[i][curr]
            take=fun(i+1,curr-nums[i])
            nt=fun(i+1,curr)
            dp[i][curr] = take or nt
            return dp[i][curr]
        return fun(0,target)