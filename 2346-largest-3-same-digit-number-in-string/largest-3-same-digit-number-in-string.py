class Solution:
    def largestGoodInteger(self, num: str) -> str:
        x=""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                c=num[i]+num[i+1]+num[i+2]
                x=max(c,x)
        if len(x)>=2:
            return x
        else:
            return ""