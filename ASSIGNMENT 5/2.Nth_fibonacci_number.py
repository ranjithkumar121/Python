def fibonacciNumbers(n):
    f1=0
    f2=1
    lst=[]
    if n<1:
        return
    lst.append(f1)
    for i in range(1,n):
        lst.append(f2)
        next=f1+f2
        f1=f2
        f2=next
    print(lst[-1])

num=int(input("Enter the value:"))
fibonacciNumbers(num)