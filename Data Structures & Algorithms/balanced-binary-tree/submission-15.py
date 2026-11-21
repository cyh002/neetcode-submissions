# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def height(node):
            if not node or not self.res:
                return 0
            left, right = height(node.left), height(node.right)
            if abs(left - right) > 1:
                self.res = False
            return max(left, right) + 1

        height(root)
        return self.res