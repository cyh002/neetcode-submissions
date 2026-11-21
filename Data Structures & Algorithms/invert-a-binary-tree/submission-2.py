# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. Base case
        # 2. Recursive Case
        # 3. Progress towards the Base Case
        # 4. Combine the results
        # base case:
        if not root:
            return
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left , root.right = right, left
        return root
