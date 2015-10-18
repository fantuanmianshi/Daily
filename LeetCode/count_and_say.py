"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""


class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if n < 1:
            return ''
        result = '1'

        i = 2
        while i <= n:
            temp, count, prev = '', 1, result[0]
            j = 1
            while j < len(result):
                if result[j] == prev:
                    count += 1
                else:
                    temp += str(count)
                    temp += prev
                    count = 1
                    prev = result[j]
                j += 1
            temp += str(count)
            temp += prev
            result = temp
            i += 1

        return result
