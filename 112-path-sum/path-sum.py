# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        found=False
        def fun(curroot,currsum):
            nonlocal found
            if curroot==None:
                return
            currsum+=curroot.val
            if curroot.left==None and curroot.right==None:
                if currsum==targetSum:
                    found=True
                return 
            if curroot.left!=None:
                fun(curroot.left,currsum)
            if curroot.right!=None:
                fun(curroot.right,currsum)
        fun(root,0)
        return found