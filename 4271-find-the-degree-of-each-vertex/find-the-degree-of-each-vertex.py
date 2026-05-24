class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        x = []
        for i in range(len(matrix)):
            x.append(sum(matrix[i]))
        return x