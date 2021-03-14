num1=int(input())
r=str(num1)
for i in r:
    num2=r[::-1]
if num1==int(num2):
    print("yes")
else:
    print("no")