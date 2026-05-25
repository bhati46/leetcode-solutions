class Solution:
    def reverseBits(self, n: int) -> int:
        x=""
        for i in range(32):
            x+=str(n%2)
            n//=2
        return int(x,2)