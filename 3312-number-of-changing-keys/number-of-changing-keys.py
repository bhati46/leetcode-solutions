class Solution:
    def countKeyChanges(self, s: str) -> int:
        c=0
        s=s.lower()
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                c+=1
        return c

