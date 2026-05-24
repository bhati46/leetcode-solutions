class Solution:
    def maxProduct(self, n: int) -> int:
        a = list(map(int, str(n)))
        a.sort()
        return a[-1]*a[-2]