def count_numbers(x,b):
    count = 0
    for i in range(1, b + 1):
        if i%2==0:
            if i % x == 0:
                count += 1
            else:
                pass
        else:
            pass
    return(count)
x=int(input())
b=int(input())
print(count_numbers(x,b))