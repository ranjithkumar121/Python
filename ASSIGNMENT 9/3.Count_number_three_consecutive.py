'''lst=list(map(int,input().split()))
count=0
for i in range(len(lst)):
    if i!=0 and i!=len(lst)-1 and i!=len(lst)-2:
        if lst[i]<0 and lst[i+1]<0 and lst[i+2]<0 and lst[i-1]>0:
            count+=1
    elif i==0:
        if lst[i]<0 and lst[i+1]<0:
            count+=1
print(count)'''
#10 7 4 5 9 12 4 3 11 13 17 5 6 96 4
lst=list(map(int,input().split()))
count=0
while(len(lst)>0):
    if lst[0]<0 and lst[1]<0 and lst[2]<0:
        lst.remove(lst[0])
        lst.remove(lst[0])
        lst.remove(lst[0])
        count+=1
    else:
        lst.remove(lst[0])

print(count)
