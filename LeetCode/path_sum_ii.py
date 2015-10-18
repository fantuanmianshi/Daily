"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's
sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
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
    # @return {integer[][]}
    def pathSum(self, root, sum):
        if root is None:
            return []
        result = []
        self.solver(root, 0, sum, [], result)
        return result

    def solver(self, root, s, target, solution, result):
        if root is None:
            return

        solution.append(root.val)
        s += root.val
        if root.left is None and root.right is None and target == s:
            result.append(solution[:])

        self.solver(root.left, s, target, solution, result)
        self.solver(root.right, s, target, solution, result)
        solution.pop()
