class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        y=0
        for row in accounts:
            x=sum(row)
            y=max(y,x)
        return y