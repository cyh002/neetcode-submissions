# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# this question is tricky as the answer u record and the return is different: 
# 1. return : the depth of the node
# 2. record: the diameter of the node. 
class Solution:
    def dfs(self, node):
        if not node:
            return 0
        left, right = self.dfs(node.left), self.dfs(node.right)
        # record the sum or diameter at that node. 
        self.res = max(self.res, left + right)
        # return the depth of the node
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root):
        self.res = 0          # reset here, every call
        self.dfs(root)
        return self.res