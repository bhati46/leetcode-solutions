class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        def fun(i,j):
            if n==i:
                return True
            if m==j:
                return False
            if s[i]==t[j]:
                return fun(i+1,j+1)
            else:
                return fun(i,j+1)
        return fun(0,0)