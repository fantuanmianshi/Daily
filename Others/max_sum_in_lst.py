'''
动态规划系列1：最大连续和

输入一个整形数组，数组里有正数也有负数。数组中连续的一个或多个整数组成一个子数组，每个子数组都有一个和。 求所有子数组的和的最大值。

样例输入：[1, -2, 3, 10, -4, 7, 2, -5]

样例输出：18 
'''

def max_sum_in_lst(lst):
    cur_sum, max_sum = 0, 0
    for i in lst:
        cur_sum = i if i > cur_sum + i else cur_sum + i
        max_sum = cur_sum if cur_sum > max_sum else max_sum
    return max_sum

test_lst = [1, -2, 3, 10, -4, 7, 2, -5]
print max_sum_in_lst(test_lst)
