"""
Given a sorted linked list, delete all duplicates such that each element appear
only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None:
            return head

        pre = None
        temp = head
        while temp is not None:
            if pre is not None:
                if pre.val != temp.val:
                    pre.next = temp
                    pre = temp
            else:
                pre = temp
            temp = temp.next
        pre.next = None

        return head
