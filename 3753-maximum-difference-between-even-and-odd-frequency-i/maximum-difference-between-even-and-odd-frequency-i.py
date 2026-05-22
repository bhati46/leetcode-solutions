from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        a=float('inf')
        b=0
        x=Counter(s)
        for i in x:
            if x[i]%2==0:
                a=min(a,x[i])
            else:
                b=max(b,x[i])
        return b-a