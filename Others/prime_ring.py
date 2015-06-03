"""
输入正整数n，把整数1,2,3,…,n (n<=16)组成一个环，使得相邻两个整数之和均为素数。输出从整数1开始，同一个环应该恰好输出一次。

样例输入：6

样例输出：

[1, 4, 3, 2, 5, 6]
[1, 6, 5, 2, 3, 4]
"""

from math import sqrt
from copy import copy

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# pre-calculated prime list for quick lookup
prime_lst = [is_prime(i) for i in xrange(0,50)]

def search(remaining_lst, result_lst):
    global prime_list
    if remaining_lst == [] \
       and prime_lst[result_lst[0] + result_lst[-1]]:
        print result_lst
    else:
        for i in remaining_lst:
            remaining_lst_copy = copy(remaining_lst)
            result_lst_copy = copy(result_lst)
            if result_lst == [] or prime_lst[i + result_lst[-1]]:
                remaining_lst_copy.remove(i)
                result_lst_copy.append(i)
                search(remaining_lst_copy, result_lst_copy)

def prime_ring(N):
    search(range(2, N+1), [1])

prime_ring(6)
