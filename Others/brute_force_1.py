"""
输入正整数n，按照从小到大顺序输出所有形如abcde/fghij=n的表达式，其中a~j恰好是数字0~9的一个排列，2<=n<=79

样例输入：62

样例输出：

79546/01283=62

94736/01528=62
"""

def brute_force_1(n):
    a = 01234
    while a * n <= 98765:
        if validate(a, a * n):
            # print result as required
            print '%05d' %  (a*n) + '/' + '%05d' % a + '=' + str(n)
        a += 1

def validate(a, b):
    '''validate whether a and b has 10 different digits'''
    digit_set = set()
    for i in range(5):
        digit_set.add(a % 10)
        a = a / 10
        digit_set.add(b % 10)
        b = b / 10
    return digit_set == set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
