lst=list(map(int,input().split()))
x=int(input())
lst1=[]

for i in lst:
    if len(lst1)<x:
        if i<0:
            lst1.append(i)

print(sum(lst1))