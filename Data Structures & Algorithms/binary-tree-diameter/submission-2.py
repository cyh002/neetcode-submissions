# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # why is this question not the same as the max depth? 
        # sum of the max depth of left and right
        if not root:
            return 0
        res = 0
        ld, rd = self.maxDepth(root.left), self.maxDepth(root.right)
        summed = ld + rd
        res = max(res, summed)
        lb = self.diameterOfBinaryTree(root.left)
        rb = self.diameterOfBinaryTree(root.right)
        res = max(res, lb, rb)
        return res
