"""
Given n, generate all structurally unique BST's (binary search trees) that
store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        return self.solver(1, n)

    def solver(self, start, end):
        result = []
        if start > end:
            result.append(None)
            return result

        i = start
        while i <= end:
            left = self.solver(start, i - 1)
            right = self.solver(i + 1, end)

            for ln in left:
                for rn in right:
                    node = TreeNode(i)
                    node.left = ln
                    node.right = rn
                    result.append(node)
            i += 1

        return result
