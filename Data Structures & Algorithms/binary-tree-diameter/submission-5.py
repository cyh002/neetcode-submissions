# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.res = 0 

    def dfs(self, root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        left, right = self.dfs(root.left), self.dfs(root.right)
        self.res = max(self.res, left + right)
        return 1 + max(left, right)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # why is this question not the same as the max depth? 
        # sum of the max depth of left and right
        if not root:
            return 0
        self.dfs(root)
        return self.res