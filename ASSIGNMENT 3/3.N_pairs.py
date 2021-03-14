n=int(input())
lst1=[]
for i in range(n):
    x=int(input())
    lst1.append(x)
z=int(input())
lst2=[]
for i in lst1:
    y=z-i
    lst2.append(y)
for i in range(len(lst1)):
    print(lst1[i],end=",")
    print(lst2[i])