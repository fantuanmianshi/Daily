"""

"""


def solution(A):
    # n, m should be given
    # otherwise n, m = min(A), max(A)
    return sum(A) - 1/2 * (n + m) * (m - n + 1)
