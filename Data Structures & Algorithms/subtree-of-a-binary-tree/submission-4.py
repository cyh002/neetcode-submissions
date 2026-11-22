# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def same(self, root, subRoot):
        # both empty:
        if not root and not subRoot:
            return True
        # if one empty and the other not:
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        # if both same
        left_same = self.same(root.left, subRoot.left)
        right_same = self.same(root.right, subRoot.right)
        return left_same and right_same

    def compare(self, root, subRoot):
        if self.same(root, subRoot):
            self.flag = True
        if root and not self.flag:
            self.compare(root.left, subRoot)
            self.compare(root.right, subRoot)
        return self.flag
          
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        self.flag = False
        self.compare(root,subRoot)
        return self.flag
      