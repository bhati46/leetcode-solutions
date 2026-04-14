class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x=[]
        for i in range(len(operations)):
            if operations[i] not in ["D", "C", "+"]:
                x.append(int(operations[i]))
            elif operations[i]=="D":
                x.append(2 * x[-1])
            elif operations[i]=="C":
                x.pop()
            elif operations[i]=="+":
                x.append(x[-1] + x[-2])
        return sum(x)