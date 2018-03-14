'''
https://projecteuler.net/problem=36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
i = 0
sum = 0
while i <= 1000000:
    dec_i = str(i)
    bin_i = bin(i)[2:]
    if dec_i == dec_i[::-1] and bin_i == bin_i[::-1]:
        sum += i
        print(dec_i,bin_i)
    i+=1
print('the sum is ',sum)