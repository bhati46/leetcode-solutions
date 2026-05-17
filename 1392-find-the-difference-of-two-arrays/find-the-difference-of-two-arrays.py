class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x=set(nums1)
        y=set(nums2)
        a = []
        a.append(list(x-y))
        a.append(list(y-x))
        return a