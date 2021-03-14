lst=list(input().split())
lst1=[]
count=0
maxi=0
n=0
for i in lst:
    for j in i:
        lst1.append(j)
print(lst1)
for i in lst1:
    count=lst1.count(i)
    if count>maxi:
        maxii=count
        n=int(i)
    elif count==maxi:
        if n<int(i):
            n=int(i)
            maxi=count


print(n)
