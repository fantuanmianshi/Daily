"""
对于输入n <= 10^6，计算 S=1! + 2! + 3! + ... + n! 的最后6位。
"""

def sum_of_factorial(n):
    if n > 25:
        n = 25
    facts = [1]  # list for factorial numbers
    for i in range(n):
        facts.append(facts[i] * (i+1) % 1000000)
    return sum(facts[1:]) % 1000000
