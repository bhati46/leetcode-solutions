class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n=len(nums)
        dp=[1]*(n)
        par=[-1]*(n)
        maxi=0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] ==0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        par[i] = j
            if dp[i] > dp[maxi]:
                maxi = i
        ans = []
        while maxi != -1:
            ans.append(nums[maxi])
            maxi = par[maxi]
        return ans[::-1]