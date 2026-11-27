# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        ans=True
        def fun(cur1,cur2):
            nonlocal ans
            if ans == False:
                return
            if cur1 == None and cur2 == None:
                return
            if cur1 == None or cur2 == None:
                ans = False
                return
            if cur1.val != cur2.val :
                ans = False
                return
            fun(cur1.left,cur2.left)
            fun(cur1.right,cur2.right)
        fun(p,q)
        return ans