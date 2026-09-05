class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        d=[[0]*(i+1) for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(i+1):
                if j == 0 or j==i:
                    d[i][j] = 1
                else:
                    d[i][j] = d[i-1][j] + d[i-1][j-1]
        return d[rowIndex]