class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        dp=[[[-1 for _ in range(len(s3))] for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        def fun(i,j,k):
            if k==len(s3) and i==len(s1) and j==len(s2):
                return True
            if dp[i][j][k]!=-1:
                return dp[i][j][k]
            take = False
            nt = False
            if i<len(s1) and s1[i]==s3[k]:
                take=fun(i+1,j,k+1)
            if j<len(s2) and s2[j]==s3[k]:
                nt=fun(i,j+1,k+1)
            dp[i][j][k]=take or nt
            return dp[i][j][k]
        return fun(0,0,0)