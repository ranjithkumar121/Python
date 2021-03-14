def find_count(num):
    c = 0
    for i in num:
        count = num.count(i)
        if count == 1:
            c += 1
        else:
            pass
    return c
num=input()
print(find_count(num))
