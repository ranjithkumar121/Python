a=[10,20,30,55]
b=[20,40,81]
c=[]
for i in a:
    if i not in b:
        c.append(i)
for i in b:
    if i not in a:
        c.append(i)
print(c)
sums=sum(c)
def sum_of_digits(a):
    ss=0
    while(a>0):
        ss=ss+int(a%10)
        a=int(a/10)
    return ss
while(len(str(sums))>1):
    sums=sum_of_digits(sums)
print(sums)