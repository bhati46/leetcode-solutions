class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if (n<=0):
             return False
        for i in range(100):
            if pow(3,i)==n:
                return True
        return False
        