class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        g=0
        x=0
        for i in gain:
            g+=i
            x=max(x,g)
        return x
        