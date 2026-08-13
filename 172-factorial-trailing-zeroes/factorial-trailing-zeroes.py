class Solution:
    def trailingZeroes(self, n: int) -> int:
        x=0
        while n>=5:
            n//=5
            x+=n
        return x