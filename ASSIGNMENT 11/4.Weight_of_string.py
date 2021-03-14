import string
alp=list(string.ascii_lowercase)
sum=0
word=input().lower()
for i in word:
    if i in alp:
        a=alp.index(i)
        sum+=a+1
print(sum)