n=int(input())
lst=[]
for i in range(n):
    a=int(input())
    if len(lst)==0:
        lst.append(a)
    else:
        if a>lst[-1]:
            lst.append(a)
        else:
            break
print(len(lst))


