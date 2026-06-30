class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        x = set()
        y = set()
        ans = []
        for i in range(len(A)):
            x.add(A[i])
            y.add(B[i])
            ans.append(len(x & y))
        return ans