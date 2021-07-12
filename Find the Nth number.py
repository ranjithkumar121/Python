lst=[]
n=int(input())
def FindNthdigit(n):
    for i in range(1,10000):
        if len(lst)==n:
            break
        a=str(i)
        if len(a)==1:
            if (a=="3" or a=="4"):
                lst.append(int(a))
        elif len(a)==2:
            if (a[0]=="3" or a[0]=="4") and (a[1]=="3" or a[1]=="4"):
                lst.append(int(a))
        elif len(a)==3:
            if (a[0] == "3" or a[0] == "4") and (a[1] == "3" or a[1] == "4") and (a[2]=="3" or a[2]=="4"):
                lst.append(int(a))
        else:
            if (a[0] == "3" or a[0] == "4") and (a[1] == "3" or a[1] == "4") and (a[2] == "3" or a[2] == "4") and (a[3]=="3" or a[3]=="4"):
                lst.append(int(a))
    return lst[-1]

print(FindNthdigit(n))

