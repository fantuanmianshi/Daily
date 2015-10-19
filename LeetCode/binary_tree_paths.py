"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if root is None:
            return result
        self.solver(root, result, str(root.val))
        return result

    def solver(self, root, result, ans):
        if root.left is None and root.right is None:
            result.append(ans)
        if root.left:
            self.solver(root.left, result, ans + '->' + str(root.left.val))
        if root.right:
            self.solver(root.right, result, ans + '->' + str(root.right.val))
