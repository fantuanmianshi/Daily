"""
Given preorder and inorder traversal of a tree, construct the binary tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        return self.solver(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
        
    def solver(self, preorder, i, j, inorder, n, m):
        if i > j or n > m:
            return None
        root = TreeNode(preorder[i])
        index = inorder.index(root.val)
        root.left = self.solver(preorder, i + 1, index - n + i, inorder, n, index - 1)
        root.right = self.solver(preorder, i + index - n + 1, j, inorder, index + 1, m)
        return root
