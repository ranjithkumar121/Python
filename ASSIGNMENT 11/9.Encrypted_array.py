lst=list(map(int,input().split()))
lst1=[]
s=0
for i in reversed(range(len(lst))):
    if lst[i]==lst[-1]:
        lst1.append(lst[i])
        s=lst[i]
    else:
        a=lst[i]-s
        lst1.append(a)
        s=a
lst1.reverse()
print(lst1)
