def LastTwoDigit(number):
    ls = str(number)
    if len(ls) == 1:
        return ls
    else:
        return ls[-2:]

number = int(input("Enter the number:"))
print(LastTwoDigit(number))