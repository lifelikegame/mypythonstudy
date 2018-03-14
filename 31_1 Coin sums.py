'''
https://projecteuler.net/problem=31
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''
sum=0
count=0
for i in range(0,2):
    for j in range(0,3-2*i):
        for k in range(0,5-2*j):
            for l in range(0,11-2*k):
                for m in range(0,21-2*l):
                    for n in range(0,41-2*m):
                        for o in range(0,101-2*n):
                            for p in range(0,201-2*o):
                                sum=i*200+j*100+k*50+l*20+m*10+n*5+o*2+p*1
                
                                if sum ==200:
                                    count+=1
                                    sum=0
                                    print(count)
                                else:
                                    sum=0
print('the sum is ',count)
