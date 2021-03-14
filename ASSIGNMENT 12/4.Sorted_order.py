def printorder(n,lst,option):
    if option==1:
        lst.sort()
        for i in range(n):
            print(lst[i],end=" ")
    elif option==2:
        lst.sort()
        lst.reverse()
        for i in range(n):
            print(lst[i],end=" ")
n=int(input())
lst=list()
option=int(input())
for i in range(n):
    l=lst.append(int(input()))
printorder(n,lst,option)