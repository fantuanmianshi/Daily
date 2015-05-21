"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
"""


from collections import defaultdict

def sort_colors_1(self, A):
    s, t, e = 0, 0, len(A) - 1
    while s <= e:
        if A[s] == 0:
            if s != t:
                A[s], A[t] = A[t], A[s]
            s, t = s + 1, t + 1
        elif A[s] == 1:
            s = s + 1
        elif A[s] == 2:
            if s != e:
                A[s], A[e] = A[e], A[s]
            e = e - 1
    return A
    
def sort_colors_2(A):
    ht = {}                          # a hash map
    ht = defaultdict(lambda: 0, ht)  # with default value 1
    for i in A:
        ht[i] += 1
    ret = []
    for k in [0, 1, 2]:
        ret.extend([k] * ht[k])
    return ret
