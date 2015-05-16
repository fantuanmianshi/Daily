
import math


class SolutionTLE:
    def isPrime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        for x in range(2, int(math.sqrt(n)) + 1):
            if n % x == 0:
                return False
        return True

    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count


class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        isPrime = [True] * max(n, 2)
        isPrime[0], isPrime[1] = False, False
        x = 2
        while x * x < n:
            if isPrime[x]:
                p = x * x
                while p < n:
                    isPrime[p] = False
                    p += x
            x += 1
        return sum(isPrime)
