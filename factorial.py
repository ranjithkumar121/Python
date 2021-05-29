def factorial(n):
    if n<0:
        return 1
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        while(n>1):
            fact=fact*n
            n=n-1
        return fact
number = int(input('Enter the number :'))
print("The factorial of",number,"is",factorial(number))

