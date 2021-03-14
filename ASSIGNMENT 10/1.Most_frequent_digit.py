def most_frequent(num):
    count = 0
    maxi = 0
    for i in num:
        count = num.count(i)
        if count > maxi:  # Here > displays smallest num if tie  and >= displays largest if tie
            maxi = count
            n = i
    return n


num=input()
print(most_frequent(num))
