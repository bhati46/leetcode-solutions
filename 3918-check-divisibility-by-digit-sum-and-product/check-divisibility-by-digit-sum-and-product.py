class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x=n
        sumx=0
        pro=1
        while n>0:
            digit=n%10
            sumx+=digit
            pro*=digit
            n //=10
        return x%(sumx+pro)==0