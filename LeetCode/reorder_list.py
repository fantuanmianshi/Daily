"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if head is None:
            return head
        fast, slow = head, head
        while True:
            fast = fast.next
            if fast is None:
                break
            fast = fast.next
            if fast is None:
                break
            slow = slow.next

        if slow is None:
            return

        # Reverse second half of the linked list
        cur, pre = slow, slow.next
        cur.next = None
        while pre is not None:
            temp = pre.next
            pre.next = cur
            cur = pre
            pre = temp

        # Merge two lists
        first, second = head, cur
        while second is not None and first is not None and first != second:
            temp = second.next
            second.next = first.next
            first.next = second
            first = second.next
            second = temp
