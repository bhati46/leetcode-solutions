class Solution:
    def tribonacci(self, n: int) -> int:
        def fun(n,a,b,c):
            if n==0:
                return a
            if n==1:
                return b
            if n==2:
                return c
            return fun(n-1,b,c,a+b+c)
        return fun(n,0,1,1)
