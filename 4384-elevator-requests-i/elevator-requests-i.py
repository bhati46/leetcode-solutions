class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        x=0
        y=0
        for i in requests:
            x+=abs(y-i)
            y=i
        return x