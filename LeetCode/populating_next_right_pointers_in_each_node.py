"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next
right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same
level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        stack = [root]
        while stack:
            i = 1
            while i < len(stack):
                stack[i - 1].next = stack[i]
                i += 1

            new_stack = []
            while stack:
                item = stack.pop(0)
                if item.left is not None:
                    new_stack.append(item.left)
                if item.right is not None:
                    new_stack.append(item.right)
            stack = new_stack


if __name__ == '__main__':
    n1 = TreeLinkNode(1)
    n2 = TreeLinkNode(2)
    n3 = TreeLinkNode(3)

    n1.left = n2
    n1.right = n3

    s = Solution()
    s.connect(n1)

    print n1.next.val
    print n2.next.val
    print n3.next.val
