class Solution:
    def greatestLetter(self, s: str) -> str:
        x=set(s)
        s=""
        for i in x:
            if i.islower()  and i.upper() in x:
                s=max(s,i.upper())
        return s