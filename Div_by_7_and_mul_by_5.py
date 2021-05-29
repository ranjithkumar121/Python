def div_mul():
    lst=[]
    for i in range(1,101):
        if i%7==0 and i%5==0:
            lst.append(str(i))
    return lst

res=div_mul()
print(','.join(res))
