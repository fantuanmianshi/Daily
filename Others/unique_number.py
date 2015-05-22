"""
一个数组A包含元素{n_1, …, n_m} 总共m个整数。已知除了一个元素外，其余的数字均出
现了两次。编程求出只出现一次的这个数字。
样例输入: [1, 2, 3, 2, 1]
样例输出: 3
"""


from collections import defaultdict


# solution 1
def special_single_number_1(lst):
    ht = {}                          # a hash map
    ht = defaultdict(lambda: 0, ht)  # with default value 1
    for i in lst:
        ht[i] += 1
    for k, v in ht.iteritems():
        if v == 1:
            return k


# solution 2
def special_single_number_2(lst):
    # xor the whole list
    return reduce(lambda x, y: x ^ y, lst)
