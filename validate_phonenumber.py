#Validating phone numbers

import string
n=int(input())
lst=string.ascii_lowercase
lst1=string.ascii_uppercase
lst2=[]
for i in range(n):
    pno =input()
    lst2=[]
    if pno[0] in ['9','8','7']:
        for j in pno:
            if j not in lst and j not in lst1:
                lst2.append(j)
        if len(pno)==10 and len(lst2)==10:
            print("YES")
        else:
            print("NO")
    else:
        print("NO") 

#Another simple method
n=int(input())
for i in range(n):
    pno =input()
    if len(pno)==10:
        if pno.isnumeric():
            if pno[0] in ['9','8','7']:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
