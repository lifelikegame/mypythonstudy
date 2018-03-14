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




            


