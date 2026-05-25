class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        x=""
        for i in b:
            x+=str(i)
        y=int(x)
        return pow(a, y, 1337)