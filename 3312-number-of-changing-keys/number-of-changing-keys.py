class Solution:
    def countKeyChanges(self, s: str) -> int:
        c=0
        for i in range(len(s)-1):
            if s[i].lower()!=s[i+1].lower():
                c+=1
        return c

