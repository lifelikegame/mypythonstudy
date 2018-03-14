"""
https://projecteuler.net/problem=5
"""
i=1
while i:
    c=0
    for j in range(1,21):
        if i%j!=0:
            c+=1
    i+=1
    if c==0:
        print('final=',i-1)
        i=0