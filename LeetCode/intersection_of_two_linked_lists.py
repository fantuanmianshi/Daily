"""
Write a program to find the node at which the intersection of two singly
linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

* If the two linked lists have no intersection at all, return null.
* The linked lists must retain their original structure after the function
  returns.
* You may assume there are no cycles anywhere in the entire linked structure.
* Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        lengthA, tempA = 0, headA
        while tempA.next is not None:
            lengthA += 1
            tempA = tempA.next

        lengthB, tempB = 0, headB
        while tempB.next is not None:
            lengthB += 1
            tempB = tempB.next

        if tempA != tempB:
            return None

        tempA, tempB = headA, headB
        diff = abs(lengthA - lengthB)
        if lengthA > lengthB:
            while diff != 0:
                tempA = tempA.next
                diff -= 1
        else:
            while diff != 0:
                tempB = tempB.next
                diff -= 1

        while tempA is not None and tempB is not None:
            if tempA == tempB:
                return tempA
            tempA = tempA.next
            tempB = tempB.next

        return None
