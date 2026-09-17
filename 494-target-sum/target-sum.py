class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n=len(nums)
        total=sum(nums)
        dp=[[-1 for _ in range(2*total+1)] for _ in range(n+2)]
        def memo(i,cursum):
            if i==0:
                return 1 if cursum == target else 0
            index=cursum+total
            if dp[i][index]!=-1:
                return dp[i][index]
            minus=memo(i-1,cursum-nums[i-1])
            plus=memo(i-1,cursum+nums[i-1])
            dp[i][index]=minus+plus
            return dp[i][index]
        return memo(n,0)