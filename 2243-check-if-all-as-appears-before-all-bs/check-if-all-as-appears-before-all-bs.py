class Solution:
    def checkString(self, s: str) -> bool:
        x=Counter(s)
        if len(set(s))==1:
            return True
        a=0
        for i in range(len(s)):
            if s[i]=="a":
                a+=1
            else:
                break
        return a==x['a']