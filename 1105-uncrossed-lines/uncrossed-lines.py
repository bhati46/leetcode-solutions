class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        dp=[[-1]*len(nums2) for _  in range(len(nums1))]
        def fun(i,j):
            if i==len(nums1) or j==len(nums2):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            take=0
            if nums1[i]==nums2[j]:
                take=1+fun(i+1,j+1)
            else:
                take=max(fun(i+1,j),fun(i,j+1))
            dp[i][j]=take
            return dp[i][j]
        return fun(0,0)