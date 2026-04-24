class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c=0
        x=0
        for i in moves:
            if i=="U":
                c+=1
            elif i=="D":
                c-=1
            elif i=="L":
                x+=1
            else:
                x-=1
        return c==0 and x==0