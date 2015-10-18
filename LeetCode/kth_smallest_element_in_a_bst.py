"""
Given a binary search tree, write a function kthSmallest to find the kth
smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need
to find the kth smallest frequently? How would you optimize the kthSmallest
routine?

Hint:

1. Try to utilize the property of a BST.
2. What if you could modify the BST node's structure?
3. The optimal runtime complexity is O(height of BST).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        result = []
        self.midorder_traversal(root, result)
        return result[k - 1]

    def midorder_traversal(self, root, result):
        if root is None:
            return
        self.midorder_traversal(root.left, result)
        result.append(root.val)
        self.midorder_traversal(root.right, result)
