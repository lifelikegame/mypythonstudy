'''
https://projecteuler.net/problem=9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
from random import randint
while True:
    a = randint(1, 500)
    b = randint(1, 500)
    if a**2+b**2 == (1000-a-b)**2:
        print(str(a)+' '+str(b)+' '+str(1000-a-b))
        print('the product is ', a*b*(1000-a-b))
        break