class Solution:
    def removeStars(self, s: str) -> str:
        x=[]
        for i in s:
            if i=="*":
                x.pop()
            else:
                x.append(i)
        return "".join(x)