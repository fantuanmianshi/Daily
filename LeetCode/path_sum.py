"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        return self.solver(root, 0, sum)
    
    def solver(self, root, sum, target):
        if root is None:
            return False
        sum += root.val
        if root.left is None and root.right is None:
            return sum == target
        left_sum = self.solver(root.left, sum, target)
        right_sum = self.solver(root.right, sum, target)
        return left_sum or right_sum
