"""
https://projecteuler.net/problem=14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def Collatz_Problem(n):
    s=[n]
    while n>1:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        s.append(n)
    return len(s)

count=999999
max=1
x=0
while count>1:
    c_p=Collatz_Problem(count)
    if c_p>max:
        max=c_p
        num=count
    count-=1
    x+=1
    if x>1000:
        print(count)
        x=0
print(max,num)