lst=list(map(int,input().split()))
for i in range(len(lst)-1):
    if lst[i]%2==1:
        print(lst[i],end=' ')
        if lst[i]%2==1 and lst[i+1]%2==1:
            pass
        else:
            print()
if lst[-1]%2==1:
    print(lst[-1])


