class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        x=len(temperatures)
        y=[]
        ans=[0]*x
        for i in range(x-1,-1,-1):
            while(len(y)!=0 and temperatures[i]>=temperatures[y[-1]]):
                y.pop()
            if len(y)!=0:
                ans[i]=y[-1]-i
            y.append(i)
        return ans
