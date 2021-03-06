'''
https://projecteuler.net/problem=28


Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''
def sum_of_diagonals(n):
    sum_of_diag=1
    number=1
    if n%2==0:
        print('n must be odd number!')
    elif n<=2:
        print('n can\'t be less than 3!')
    else:
        for i in range(3,n+1,2):
            for j in range(4):
                number+=(i-1)
                sum_of_diag+=number
        return sum_of_diag

print(sum_of_diagonals(1001))



