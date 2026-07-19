class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        x=[]
        i=1
        while(i<=n):
            if n%i==0:
                x.append(i)
            i+=1
        return x[k-1] if len(x) >= k else -1