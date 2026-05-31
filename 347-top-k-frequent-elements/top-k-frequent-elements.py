from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x=Counter(nums)
        y = sorted(x, key=x.get, reverse=True)
        return y[:k]