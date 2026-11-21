# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:        # both empty → same
            return True
        if not p or not q:         # exactly one empty → different
            return False
        if p.val != q.val:         # compare values, not node objects
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)