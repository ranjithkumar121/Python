num=int(input())
sum=0
while(num!=0):
    sum=sum+int(num%10)
    num=num//10
print(sum)