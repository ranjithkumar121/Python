#10 7 4 5 9 12 4 3 11 13 17 5 6 96 4
lst=list(map(int,input().split()))
count=0
while(len(lst)>0):
    if lst[0]%2==1 and lst[1]%2==1:
        lst.remove(lst[0])
        lst.remove(lst[0])
        count+=1
    else:
        lst.remove(lst[0])

print(count)

