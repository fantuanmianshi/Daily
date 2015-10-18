"""
Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
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
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        whole_tree = []
        stack = [root]
        while stack:
            new_stack = []
            whole_tree.append(stack[:])
            while stack:
                item = stack.pop(0)
                if item.left is not None:
                    new_stack.append(item.left)
                if item.right is not None:
                    new_stack.append(item.right)
            stack = new_stack

        result = []
        for i, v in enumerate(whole_tree):
            if i % 2 != 0:
                result.append([n.val for n in v][::-1])
            else:
                result.append([n.val for n in v])
        return result
