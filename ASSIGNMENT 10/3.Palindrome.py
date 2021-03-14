n=input()
lst=[]
for i in range(len(n)):
    count=1
    for j in range(len(n)):
        if i!=j:
            if n[i]==n[j]:
                count+=1
    lst.append(count)

print(lst)
c=0
for i in lst:
    if i%2==0:
        a=1
    else:
        c=c+1
        if c>1:
            a=0
            break
if a==1:
    print("Yes")
else:
    print("No")





