"""
https://projecteuler.net/problem=12
"""
from math import sqrt
def prime_generator(n):
    pp=[2,3]
    for i in range(3,n):
        i+=2
        count=0
        for ps in pp:
            if ps>(sqrt(i)+1):
                break
            if i%ps==0:
                count+=1
                break 
        if count==0:
            pp.append(i)
    return pp

def tri_num(n):
    return int(n*(n+1)/2)

def get_prime_divisor(m):
    p=prime_generator(int(sqrt(m))+1)
    divisors=[]
    length=[]
    for i in p:
        c=0
        while True:
            if m%i==0:
                divisors.append(i)
                m=m/i
                c+=1               
            else:              
                break
        if c>0:
            length.append(c)
    number=1
    for j in length:
        number*=(j+1)
    return [divisors,length,number]
   
i=0
while True:
    i+=1
    a=get_prime_divisor(tri_num(i))
    if a[2]>500:
        print(tri_num(i),a[2])
        break


