"""
Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
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
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.solver(root.left, root.right)

    def solver(self, left, right):
        if left is None:
            return right is None
        if right is None:
            return left is None
        if left.val != right.val:
            return False
        if not self.solver(left.left, right.right):
            return False
        if not self.solver(left.right, right.left):
            return False
        return True
