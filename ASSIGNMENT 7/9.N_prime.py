def findprime(n,x):
    lst = []
    while (len(lst) < n):
        if x > 1 and x != 2:
            for i in range(2, x):
                if x % i == 0:
                    break
            else:
                lst.append(x)
        x += 1
    for i in lst:
        print(i, end=' ')
n=int(input())
x=int(input())
findprime(n,x)
