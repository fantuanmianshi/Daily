"""
Reverse a singly linked list.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseListIterative(self, head):
        if head is None:
            return head
        h, p, n = None, head, head.next
        while n is not None:
            temp = n.next
            n.next, p.next = p, h
            h = p
            p = n
            n = temp
        return p

    def reverseListRecursive(self, head):
        if head is None:
            return head
        first, rest = head, head.next
        if rest is None:
            return head

        rest = self.reverseListRecursive(rest)
        first.next.next = first
        first.next = None
        head = rest
        return head
