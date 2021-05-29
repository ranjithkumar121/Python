

def getSum(n):
    sumEven = 0
    c = 1

    while (n != 0):
        if (c % 2 != 0):
            sumEven += n %10

        n //= 10
        c += 1


    print("Sum even =", sumEven)

n = 457892
getSum(n)