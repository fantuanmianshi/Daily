"""
一个数组A包含元素从n到m(m>n)的连续整数。已知除了一个元素出现两次以外，其余的数字均只出现了一次。编程求出出现两次的这个数字。 
样例输入: [4,2,3,4,1,6,5] 
样例输出: 4
"""


def solution(A):
    # n, m should be given
    # otherwise n, m = min(A), max(A)
    return sum(A) - 1/2 * (n + m) * (m - n + 1)
