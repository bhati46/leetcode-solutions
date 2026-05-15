class Solution:
    def numberOfMatches(self, n: int) -> int:
        x=0
        while n>1:
            if n%2==0:
                x+=n//2
                n//=2
            else:
                x+=(n-1)//2
                n=(n-1)//2+1
        return x
            