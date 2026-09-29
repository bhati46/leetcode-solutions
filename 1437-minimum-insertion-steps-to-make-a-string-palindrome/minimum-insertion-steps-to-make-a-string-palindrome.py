class Solution:
    def minInsertions(self, s: str) -> int:
        # in problem we have counted the lcs and then returned the len(s)-lcs
        s1=s[::-1]
        n=len(s)
        dp=[[-1]*(n+1) for _ in range(n+1)]
        def fun(i,j):
            if i==n or j==n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            take=0
            if s[i]==s1[j]:
                take=1+fun(i+1,j+1)
            else:
                take=max(fun(i+1,j),fun(i,j+1))
            dp[i][j]=take
            return dp[i][j] # the whole code is same as lcs but we have to return the char we have to add to the string to make it palindrom str
        return n-fun(0,0)