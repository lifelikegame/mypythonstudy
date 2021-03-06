"""
https://projecteuler.net/problem=21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
 If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def divisor(n):
    i = 1
    div = [1]
    while i <= n / 2:
        i += 1
        if n % i == 0 and n != i:
            div.append(i)
    return sum(div)


n = 0
amicable = []
while n <= 10000:
    n += 1
    if divisor(divisor(n)) == n and n != divisor(n):
        amicable.append(n)
print(sum(amicable))
