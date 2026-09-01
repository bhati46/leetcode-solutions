class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        dp=[-1]*(n*n)
        def fun(l,r):
            if l==r:
                return piles[l]
            index = l * n + r
            if dp[index] != -1:
                return dp[index]
            al=piles[l]-fun(l+1,r)
            bo=piles[r]-fun(l,r-1)
            dp[index]=max(al,bo)
            return dp[index]
        return fun(0,n-1)>0