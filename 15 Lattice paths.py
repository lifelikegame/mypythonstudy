"""
https://projecteuler.net/problem=15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.



How many such routes are there through a 20×20 grid?
"""
import random
path=['f' for i in range(20)]+['d' for i in range(20)]
path_s=''.join(path)
all_path=set()
all_path.add(path_s)

i=100000000
c=0
while i>0:
    i-=1
    random.shuffle(path)
    path_s=''.join(path)
    if path_s not in all_path:
        all_path.add(path_s)
    c+=1
    if c>10000:
        print(i,len(all_path))
        c=0
print(len(all_path))

