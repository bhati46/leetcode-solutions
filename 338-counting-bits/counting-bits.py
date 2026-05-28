class Solution:
    def countBits(self, n: int) -> List[int]:
        y=[]
        for i in range(n+1):
            x=bin(i)[2:]
            c=0
            for j in x:
                if j=="1":
                    c+=1
            y.append(c)
        return y