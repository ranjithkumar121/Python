def sum_of(input1,input2):
    c=[]
    for i in input1:
        if i not in input2:
            c.append(i)
    for i in input2:
        if i not in input1:
            c.append(i)
    n=sum(c)
    while(n>0):
        s=0
        while(n>0):
            s+=n%10
            n=int(n/10)
        if len(str(s))>1:
            n=s
        else:
            return s
    return s

input1=[6,7,12,70,44]
input2=[8,6,70,44]
ss=sum_of(input1,input2)
print(ss)


