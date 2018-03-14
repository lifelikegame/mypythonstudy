'''
https://projecteuler.net/problem=10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from math import sqrt
def generate_prime(n):
    pp = 2
    ps = [pp]
    pp += 1
    ps.append(pp)
    while pp < n:
        pp += 2
        test = True
        sqrtpp = sqrt(pp)
        for i in ps:
            if i > sqrtpp:
                break
            if pp%i == 0:
                test = False
                break
        if test:
            ps.append(pp)
    return ps

print(sum(generate_prime(2000000)))