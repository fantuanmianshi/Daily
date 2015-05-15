
# solution 1
def solution1(A):
    for i in range(0, len(A)):
        if i == A[i]:
            return i

# solution 2
def solution2(A):
    l, r = 0, len(A) - 1
    while l <= r:
        m = (l + r) / 2
        if A[m] == m:
            return m
        elif A[m] < m:
            l = m + 1
        else:
            r = m - 1 