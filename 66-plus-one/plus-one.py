class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=0
        n=len(digits)
        r=[0]*(n+1)
        for i in range(n-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
        r[0]=1
        return r
            



            
        

            