"""
Given a binary tree, imagine yourself standing on the right side of it, return
the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if root is None:
            return []
        result = []
        stack = [root]
        while stack:
            result.append(stack[-1].val)
            new_stack = []
            while stack:
                item = stack.pop(0)
                if item.left is not None:
                    new_stack.append(item.left)
                if item.right is not None:
                    new_stack.append(item.right)
            stack = new_stack
        return result
