a=int(input())
s=a%10
if a<5:
    print(a)
else:
    if s<5:
        print(a-s)

    else:
        print(a+(10-s))