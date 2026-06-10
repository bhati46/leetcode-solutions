class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        y=0
        for i in range(left,right+1):
            x=bin(i)[2:]
            c=0
            for i in x:
                if i=="1":
                    c+=1
            if c in [2,3,5,7,11,13,17,19,23,29,31,37]:
                y+=1
        return y