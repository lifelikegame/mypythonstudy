"""
https://projecteuler.net/problem=18
"""

Number_list = []
File = open('p018_Maximum path sum I.txt', 'r')
for line in File:
    Number_list.append(list(map(int, line.strip().split())))
#print(Number_list)


def walk(i, j):
    if i == len(Number_list) - 1:
        return Number_list[i][j]
    walk_left = walk(i + 1, j)
    walk_right = walk(i + 1, j + 1)
    return Number_list[i][j] + max(walk_left, walk_right)

print(walk(0, 0))
