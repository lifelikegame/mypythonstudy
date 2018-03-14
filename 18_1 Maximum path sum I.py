"""
https://projecteuler.net/problem=18
"""

import random

number_list = []
file = open('p018_Maximum path sum I.txt', 'r')
for line in file:
    sub_list = []
    sub_list = [int(n) for n in line.strip().split(' ')]
    number_list.append(sub_list)
# print(number_list)
length = len(number_list)

# the_sum=number_list[0][0]+number_list[1][0+random.randint(0,2)]+number_list[2][0+random.randint(0,2)+0+random.randint(0,2)]
n = 0
maxmum_sum = 0
while n < 100000:
    the_sum = number_list[0][0]
    path = [number_list[0][0]]
    seed = random.randint(0, 1)
    for i in range(1, length):
        the_sum += number_list[i][seed]
        path.append(number_list[i][seed])
        seed += random.randint(0, 1)
#    print(path)
#    print(the_sum)
    if the_sum > maxmum_sum:
        maxmum_sum = the_sum
        max_path = path
    n += 1
print(max_path)
print(maxmum_sum)
