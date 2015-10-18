"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        return self.solver([head], [head])

    def solver(self, head, tail):
        if tail[0] is None:
            return True
        if self.solver(head, [tail[0].next]) and head[0].val == tail[0].val:
            head[0] = head[0].next
            return True
        else:
            return False

    def isPalindromeReverse(self, head):
        if head is None:
            return True

        # Find mid node
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        p, last = slow.next, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next

        # Check palindrome
        p1, p2 = last, head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next

        # Resume linked list(optional)
        p, last = last, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next
        slow.next = last
        return p1 is None


if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(1)

    print s.isPalindrome(n1)

    n1.next = n2
    print s.isPalindrome(n1)

    n2.next = n3
    print s.isPalindrome(n1)
