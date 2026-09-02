class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        dp = [[-1] * n for _ in range(n)]
        def fun(l,r):
            if l>r:
                return 0
            if dp[l][r] !=-1:
                return dp[l][r]
            left=piles[l]-fun(l+1,r)
            right=piles[r]-fun(l,r-1)
            dp[l][r]=max(left,right)
            return dp[l][r]
        return fun(0,n-1)>0
            