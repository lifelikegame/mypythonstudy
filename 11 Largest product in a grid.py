"""
https://projecteuler.net/problem=11
"""
file=open("p011_Largest product in a grid.txt","r")
matrix=[]
number_of_line = 0
for line in file:
    raw=line.strip().split(' ')
    matrix.append([])
    raw_to_int=[int(n) for n in raw]
    matrix[number_of_line]=raw_to_int
    number_of_line+=1
file.close()
#print(matrix)
product=[]
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        product_tmp_r=1
        for a in range(0,4):
            b=j+a
            if b>19:
                break
            product_tmp_r*=matrix[i][b]
        product.append(product_tmp_r)
        product_tmp_c=1 
        for c in range(0,4):
            d=i+c
            if d>19:
                break
            product_tmp_c*=matrix[d][j]     
        product.append(product_tmp_c)
        product_tmp_right=1
        for e in range(0,4):
            f,g=i+e,j+e
            if f>19 or g>19:
                break
            product_tmp_right*=matrix[f][g]
        product.append(product_tmp_right)
        product_tmp_left=1
        for h in range(0,4):
            k,l=i+h,j-h
            if k>19 or l<0:
                break
            product_tmp_left*=matrix[k][l]
        product.append(product_tmp_left)
print(max(product))