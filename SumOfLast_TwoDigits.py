def LastTwoDigit(number):
    ls = str(number)
    if len(ls) == 1:
        return ls
    else:
        sum = int(ls[-2])+int(ls[-1])
        return sum

number = int(input("Enter the number:"))
print(LastTwoDigit(number))