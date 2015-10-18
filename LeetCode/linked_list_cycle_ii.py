"""
Given a linked list, return the node where the cycle begins. If there is no
cycle, return null.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycleHash(self, head):
        temp = head
        repeat_map = {}

        while temp is not None:
            if temp in repeat_map:
                return temp
            repeat_map[temp] = True
            temp = temp.next

        return None

    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if fast is None or fast.next is None:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast
