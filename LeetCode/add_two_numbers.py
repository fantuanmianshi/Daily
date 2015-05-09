"""
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Notice: extra digit.
"""


class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        new_root = None

        temp_l1, temp_l2 = l1, l2
        temp = new_root
        extra_digit = 0
        while None not in [temp_l1, temp_l2]:
            value = temp_l1.val + temp_l2.val + extra_digit
            if temp is None:
                temp = ListNode(value)
                new_root = temp
            else:
                new_node = ListNode(value)
                temp.next = new_node
                temp = new_node
            if temp.val >= 10:
                temp.val -= 10
                extra_digit = 1
            else:
                extra_digit = 0
            temp_l1 = temp_l1.next
            temp_l2 = temp_l2.next

        continue_temp = temp_l1 if temp_l1 is not None else temp_l2
        while continue_temp is not None:
            value = continue_temp.val + extra_digit
            new_node = ListNode(value)
            temp.next = new_node
            temp = new_node
            if temp.val >= 10:
                temp.val -= 10
                extra_digit = 1
            else:
                extra_digit = 0
            continue_temp = continue_temp.next

        if extra_digit >= 1:
            new_node = ListNode(extra_digit)
            temp.next = new_node
            temp = new_node

        return new_root
