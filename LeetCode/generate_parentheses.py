"""
Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"

Tag: Backtracking, String
"""


class Solution1:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        result = []
        if n > 0:
            self.generateParenthesisUtil(0, 0, 0, n, [], result)
        return result

    def generateParenthesisUtil(self, left, right, num, n, solution, result):
        if num == 2 * n:
            result.append(''.join(solution))
            return
        if left < n:
            solution.append('(')
            self.generateParenthesisUtil(
                left + 1, right, num + 1, n, solution, result
            )
            solution.pop()
        if right < left:
            solution.append(')')
            self.generateParenthesisUtil(
                left, right + 1, num + 1, n, solution, result
            )
            solution.pop()


class Solution2:
    def generateParenthesis(self, n):
        if n == 1:
            return set(["()"])
        else:
            ret = set()
            for i in self.generateParenthesis(n-1):
                ret.add("()"+i)
                ret.add("("+i+")")
                ret.add(i+"()")
            return ret
