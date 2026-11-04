class Solution:
    def minCut(self, s: str) -> int:
        # dp=[[float('inf')]*len(s)]
        # dp2=[float('inf')]*len(s)
        # def fun(i,j):
        #     while i<j:
        #         if s[i]!=s[j]:
        #             return False
        #         i+=1
        #         j-=1
        #     return True
        # def solve(i,j):
        #     if i>=j or fun(i,j):
        #         dp2[i]=0
        #         return dp[i][j]
        #     if dp2[i]!=float('inf'):
        #         return dp2[i]
        #     ans=float('inf')
        #     for k in range(i,j):
        #         if fun(i,k):
        #             temp=1+solve(k+1,j)
        #             ans=min(ans,temp)
        #     dp2[i]=ans
        #     return ans
        # return solve(0,len(s)-1)-1
        n=len(s)
        dp=[[float('inf')]*len(s) for _ in range(len(s))]
        dp2=[float('inf')]*len(s)
        def fun(i,j):
            if i >= j:
                return True
            if dp[i][j]!=float('inf'):
                return dp[i][j]
            if s[i] == s[j]:
                dp[i][j] = fun(i + 1, j - 1)
            else:
                dp[i][j] = False
            return dp[i][j]
        def solve(i):
            if i==n :
                return 0
            if dp2[i]!=float('inf'):
                return dp2[i]
            ans=float('inf')
            for k in range(i,n):
                if fun(i,k):
                    temp=1+solve(k+1)
                    ans=min(ans,temp)
            dp2[i]=ans
            return ans
        return solve(0)-1