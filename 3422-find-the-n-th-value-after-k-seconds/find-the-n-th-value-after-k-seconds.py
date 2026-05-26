class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        x=[1]*n
        while(k>0):
            for i in range(len(x)):
                if i==0:
                    x[i]=x[i]
                else:
                    x[i]+=x[i-1] 
            k-=1
        return x[len(x)-1]%(10**9+7)