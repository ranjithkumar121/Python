def sum_of_digits(li):
    sum=0
    for i in li:
        while(i!=0):
            sum=sum+(i%10)
            i=i//10
    return sum

num1=int(input())
num2=int(input())
list1=[num1,num2]
res=sum_of_digits(list1)
if res%2==0:
    print("EVEN")
else:
    print("ODD")