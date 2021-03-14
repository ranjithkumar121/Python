def find_count(num):
    lst = []
    for i in num:
        if i not in lst:
            lst.append(i)
    return len(lst)
num=input()
print(find_count(num))