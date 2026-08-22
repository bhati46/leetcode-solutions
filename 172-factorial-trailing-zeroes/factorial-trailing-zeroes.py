class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fun(n):
            if n<5:
                return 0
            return n//5+fun(n//5)
        return fun(n)