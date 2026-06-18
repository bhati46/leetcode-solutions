class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        x=abs((30*hour)-(5.5*minutes))
        y=360-x
        return  x if x<y else y