# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# record the True / False
# return the maxDepth
class Solution:
    def currDiff(self, root):
        if not root:
            return 0
        left = self.currDiff(root.left)
        right = self.currDiff(root.right)
        diff =  abs(left - right)
        if diff > 1:
            self.res = False
        
        return max(left,right) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.res = True
        self.currDiff(root)
        return self.res