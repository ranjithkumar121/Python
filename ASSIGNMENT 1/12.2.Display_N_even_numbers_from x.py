n=int(input())
x=int(input())
y=int(input())
lst=[]
for i in range(y,1000):
    if i%x==0 and i%2==0:
        lst.append(i)
        if len(lst)==n:
            break
for i in lst:
    print(i,end=' ')


