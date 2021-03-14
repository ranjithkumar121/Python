n=input()
sum=0
for i in n:
    j=int(i)
    if i==n[-1]:
        sum+=j**0
        break
    else:
        sum+=j**j+1
print(sum)


