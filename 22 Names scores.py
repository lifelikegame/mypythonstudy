'''
https://projecteuler.net/problem=22
'''
dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
file_name = open('p022_names.txt','r')
str_name = file_name.read()
str_name=str_name.replace('"','')
str_list = sorted(str_name.split(','))
#print(str_list)
con = 0
score_sum=0
for i in str_list:
    con += 1
    worth = 0
    for w in i:
        worth+=dic[w]
    score=worth*con
    score_sum+=score
print(score_sum)


