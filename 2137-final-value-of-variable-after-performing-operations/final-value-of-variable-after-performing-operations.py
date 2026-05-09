class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        y=0
        for i in range(len(operations)):
            if operations[i] == "X++" or operations[i] == "++X":
                y+=1
            elif operations[i]=="--X" or operations[i] == "X--":
                y-=1
        return y
