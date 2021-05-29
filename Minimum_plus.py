eq=input()
a,b=eq.split("=")
l=len(a)
if l <= 4:
    if l == 2:
        if int(a[0]) +int(a[1]) == int(b):
            print(1)
        else:
            print(-1)
    elif l == 3:
        if int(a[0])+int(a[1:]) == int(b):
            print(1)
        elif int(a[0:2])+int(a[-1]) == int(b):
            count=1
            print(1)
        elif int(a[0])+int(a[1])+int(a[2]) == int(b):
            print(2)
        else:
            print(-1)
    else:
        if int(a[0])+int(a[1:]) == int(b):
            print(1)
        elif int(a[0:2])+int(a[2:]) == int(b):
            print(1)
        elif int(a[0:3])+int(a[3])==int(b):
            print(1)
        elif int(a[0])+int(a[1])+int(a[2:])==int(b):
            print(2)
        elif int(a[0:2])+int(a[2])+int(a[3])==int(b):
            print(2)
        elif int(a[0])+int(a[1])+int(a[2])+int(a[3])==int(b):
            print(3)
        else:
            print(-1)
