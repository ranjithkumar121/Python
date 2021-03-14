n=input().split()
lst=[]
for i in n:
    lst.append(len(i))
sums=sum(lst)
while(sums>0):
    s=0
    while(sums>0):
        s+=sums%10
        sums=int(sums/10)
    if len(str(s))>1:
        n=s
    else:
        break
print(s)

'''n=input()
for i in n.split():
    print(i)'''



