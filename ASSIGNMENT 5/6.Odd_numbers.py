x=int(input())
lst=[]
for i in range(1,1000,2):
    lst.append(i)
    if len(lst)==x:
        break
for i in lst:
    print(i)