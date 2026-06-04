class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        x=str(n)
        s=0
        for i in range(len(x)):
            s+=int(x[i])
        return s