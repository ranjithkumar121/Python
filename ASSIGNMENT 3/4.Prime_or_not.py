num = int(input())
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(0)
            break
    else:
        print(1)
else:
    print(0)