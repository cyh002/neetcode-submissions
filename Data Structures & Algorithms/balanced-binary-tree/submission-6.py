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
        left = self.currDiff(root.left)    # checks the whole left subtree, returns its height
        right = self.currDiff(root.right)  # same for the right
        if abs(left - right) > 1:
            self.res = False
        return max(left, right) + 1        # this node's height

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.currDiff(root)
        return self.res