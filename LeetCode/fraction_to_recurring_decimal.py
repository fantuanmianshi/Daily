"""
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

* Given numerator = 1, denominator = 2, return "0.5".
* Given numerator = 2, denominator = 1, return "2".
* Given numerator = 2, denominator = 3, return "0.(6)".
"""


class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        result = ''
        if denominator < 0:
            denominator = -denominator
            numerator = -numerator
        if numerator < 0:
            numerator = -numerator
            result += '-'
        result += str(numerator / denominator)

        remainder = numerator % denominator
        if remainder == 0:
            return result

        result += '.'
        save, have = [], {}
        i = 0
        while remainder and remainder not in have:
            have[remainder] = i
            remainder *= 10
            save.append(remainder / denominator)
            remainder %= denominator
            i += 1

        if remainder:
            j = 0
            while j < have[remainder]:
                result += str(save[j])
                j += 1
            result += "("
            j = have[remainder]
            while j < len(save):
                result += str(save[j])
                j += 1
            result += ")"
        else:
            j = 0
            while j < len(save):
                result += str(save[j])
                j += 1

        return result
