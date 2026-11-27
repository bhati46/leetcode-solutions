# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        # time complexity is O(n) as we are going on each node only once 
        found=False
        def fun(cur,cursum):
            nonlocal found
            if cur != None:
                cursum+=cur.val
            if cur==None:
                return 
            if cur.right == None and cur.left == None:
                if cursum==targetSum:
                    found=True
                return
            if cur.left!=None:
                fun(cur.left,cursum)
            if cur.right!=None:
                fun(cur.right,cursum)
        fun(root,0)
        return found
                
