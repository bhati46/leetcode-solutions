class Solution:
    def hammingWeight(self, n: int) -> int:
        c="" 
        while(n>0):
            c+=str(n%2)
            n//=2
        x=0 
        for i in c:
            if i=="1":
                x+=1
        return x