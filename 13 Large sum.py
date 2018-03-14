"""
https://projecteuler.net/problem=13
"""
file=open("p013_Large sum.txt","r")
sum=0
for line in file:
    sum+=int(line.strip())
sum_10=str(sum)[0:10]
print(sum_10)
