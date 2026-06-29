class Solution:
    def convertDateToBinary(self, date: str) -> str:
        x=date.split("-")
        for i in range(3):
            x[i]=bin(int(x[i]))[2:]
        return "-".join(x)