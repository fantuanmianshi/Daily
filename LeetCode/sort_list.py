"""
Sort a linked list in O(n log n) time using constant space complexity.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        p, length = head, 0
        while p is not None:
            p = p.next
            length += 1

        fake_head = ListNode(-1)
        fake_head.next = head

        i = 1
        while i <= length:
            pre, slow = fake_head, fake_head.next
            fast = fake_head.next
            while fast is not None or slow is not None:
                j = 0
                while j < i and fast is not None:
                    fast = fast.next
                    j += 1

                fvisit, svisit = 0, 0
                while fvisit < i and svisit < i and fast is not None and slow is not None:
                    if fast.val < slow.val:
                        pre.next = fast
                        pre = fast
                        fast = fast.next
                        fvisit += 1
                    else:
                        pre.next = slow
                        pre = slow
                        slow = slow.next
                        svisit += 1
                while fvisit < i and fast is not None:
                    pre.next = fast
                    pre = fast
                    fast = fast.next
                    fvisit += 1
                while svisit < i and slow is not None:
                    pre.next = slow
                    pre = slow
                    slow = slow.next
                    svisit += 1
                pre.next = fast
                slow = fast

            i *= 2

        new_head = fake_head.next
        return new_head
