# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        maxi=0
        def fun(curroot,currsum):
            nonlocal maxi
            if curroot == None:
                return 
            currsum+=1
            if curroot.right == None and curroot.left==None:
                maxi=max(currsum,maxi)
                return 
            if curroot.left != None:
                fun(curroot.left,currsum)
            if curroot.right != None:
                fun(curroot.right,currsum)
        fun(root,0)
        return maxi