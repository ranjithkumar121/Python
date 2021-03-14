def count_numbers(x,a,b):
    count = 0
    for i in range(a, b + 1):
        if i % x == 0:
            count += 1
        else:
            pass
    return(count)
x=int(input())
a=int(input())
b=int(input())
print(count_numbers(x,a,b))
