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
        def fun(curroot,currsum):
            nonlocal found # to make the var as gloal found woud be refered 
            if curroot==None:
                return
            currsum+=curroot.val # currot ki value liye hn 
            if curroot.left==None and curroot.right==None:
                if currsum==targetSum:
                    found=True
                return 
            if curroot.left!=None: # left node hai ya nhi
                fun(curroot.left,currsum)
            if curroot.right!=None: # right node hai ya nhi 
                fun(curroot.right,currsum)
        fun(root,0)
        return found