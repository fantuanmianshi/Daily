"""
Given inorder and postorder traversal of a tree, construct the binary tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        return self.solver(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def solver(self, inorder, i, j, postorder, n, m):
        if i > j or n > m:
            return None
        root = TreeNode(postorder[m])
        index = inorder.index(root.val)
        root.left = self.solver(inorder, i, index - 1, postorder, n, n + index - i - 1)
        root.right = self.solver(inorder, index + 1, j, postorder, n + index - i, m - 1)
        return root
