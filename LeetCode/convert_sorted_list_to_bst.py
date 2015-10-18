"""
Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        return self.solver([head], 0, length)

    def solver(self, head, start, end):
        if start > end or head[0] is None:
            return None
        mid = start + (end - start) / 2
        left = self.solver(head, start, mid - 1)
        root = TreeNode(head[0].val)
        head[0] = head[0].next
        right = self.solver(head, mid + 1, end)
        root.left = left
        root.right = right
        return root
