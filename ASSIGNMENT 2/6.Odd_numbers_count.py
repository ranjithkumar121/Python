N=int(input())
count=0
for i in range(N):
    num=int(input())
    if num%2==1:
        count+=1
print(count)