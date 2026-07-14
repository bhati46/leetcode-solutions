class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        x=time%(2*(n-1))
        if x<n:
            return x+1
        return 2 * n - x - 1