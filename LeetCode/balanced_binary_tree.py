"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differ by
more than 1.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if root is None:
            return True
        self.solver(root)
        return self.balanced

    balanced = True
    def solver(self, root):
        if root is None:
            return 0
        left_height = self.solver(root.left) + 1
        right_height = self.solver(root.right) + 1
        if abs(left_height - right_height) > 1:
            self.balanced = False
        return max(left_height, right_height)
