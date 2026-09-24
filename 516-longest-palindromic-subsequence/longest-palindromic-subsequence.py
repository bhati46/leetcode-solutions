class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1=s[::-1]
        dp=[[-1]*len(s) for _  in range(len(s))]
        def fun(i,j):
            if i==len(s) or j==len(s):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            take=0
            if s[i]==s1[j]:
                take=1+fun(i+1,j+1)
            else:
                take=max(fun(i+1,j),fun(i,j+1))
            dp[i][j]=take
            return dp[i][j]
        return fun(0,0)