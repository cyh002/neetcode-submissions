# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursion

        # 1. base case
        # 2. progress to the base case
        # 3. combine the results 
        if not root:
            return 0
        left , right = self.maxDepth(root.left), self.maxDepth(root.right)
        return max(left, right) + 1