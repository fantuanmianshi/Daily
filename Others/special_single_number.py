"""
一个数组A包含元素{n_1, …, n_m} 总共m个整数。已知除了两个元素外，其余的数字均出现了两次。编程求出只出现一次的这个数字。 
样例输入: [1, 2, 3, 7, 6, 2, 1, 7] 
样例输出: [3, 6]
"""


# solution 1
def special_single_number_1(lst):
    ht = {}                          # a hash map
    ht = defaultdict(lambda: 0, ht)  # with default value 0
    for i in lst:
        ht[i] += 1
    ret = []
    for k, v in ht.iteritems():
        if v == 1:
            ret.append(k)
    return ret
