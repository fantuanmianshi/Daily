"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely
filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root is None:
            return 0

        l, r = root, root
        hl, hr = 0, 0
        while l:
            l = l.left
            hl += 1
        while r:
            r = r.right
            hr += 1
        if hr == hl:
            return 2 ** hl - 1

        left_count = self.countNodes(root.left)
        right_count = self.countNodes(root.right)
        return 1 + left_count + right_count
