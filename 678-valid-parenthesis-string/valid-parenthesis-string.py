class Solution:
    def checkValidString(self, s: str) -> bool:
        dp=[[-1]*(len(s)+1) for _ in range(len(s))]
        def fun(i,c):
            if i==len(s):
                return c==0
            if c<0:
                return False
            if dp[i][c]!=-1:
                return dp[i][c]
            if s[i]=="(":
                dp[i][c]=fun(i+1,c+1)
            if s[i]==")":
                dp[i][c]=fun(i+1,c-1)
            if s[i]=="*":
                dp[i][c]=(fun(i+1,c+1) or fun(i+1,c-1) or fun(i+1,c))
            return dp[i][c]
        return fun(0,0)