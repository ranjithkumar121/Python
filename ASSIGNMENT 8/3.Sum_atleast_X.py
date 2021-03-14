n=int(input())
lst=list(map(int,input().split()))
x=int(input())
nlst=[]
for i in lst:
    if i>0 and i%2==0:
        nlst.append(i)

for i in range(len(nlst)):
    for j in range(len(nlst)):

