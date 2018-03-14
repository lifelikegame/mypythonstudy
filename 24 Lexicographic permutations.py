"""
https://projecteuler.net/problem=24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
list=[]
o=[0,1,3,4,5,6,7,8,9]
for n_9 in o:
    a=o[:]
    a.remove(n_9)
    for n_8 in a:
        b=a[:]
        b.remove(n_8)
        for n_7 in b:
            c=b[:]
            c.remove(n_7)
            for n_6 in c:
                d=c[:]
                d.remove(n_6)
                for n_5 in d:
                    e=d[:]
                    e.remove(n_5)
                    for n_4 in e:
                        f=e[:]
                        f.remove(n_4)
                        for n_3 in f:
                            g=f[:]
                            g.remove(n_3)
                            for n_2 in g:
                                h=g[:]
                                h.remove(n_2)
                                for n_1 in h:
                                    number=2*1E9+n_9*1E8+n_8*1E7+n_7*1E6+n_6*1E5+n_5*1E4+n_4*1E3+n_3*1E2+n_2*1E1+n_1
                                    list.append(number)

print(int(list[274239]))
