class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        mod=10**9+7
        x,y=pos,n-pos-1
        
        f=[1]*(n+1)
        for i in range(1,n+1): f[i]=f[i-1]*i%mod
        
        inv=[1]*(n+1)
        inv[n]=pow(f[n],mod-2,mod)
        for i in range(n,0,-1): inv[i-1]=inv[i]*i%mod
        
        def c(a,b):
            if b<0 or b>a: return 0
            return f[a]*inv[b]%mod*inv[a-b]%mod
        
        z=0
        for i in range(max(0,k-y),min(k,x)+1):
            z=(z+c(x,i)*c(y,k-i))%mod
        
        return z*2%mod
        