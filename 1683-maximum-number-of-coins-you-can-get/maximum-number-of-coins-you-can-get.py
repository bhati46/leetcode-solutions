class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        n = len(piles) // 3
        for i in range(n):
            ans += piles[len(piles) - 2 - 2 * i]
        return ans