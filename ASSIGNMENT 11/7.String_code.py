import string
n=input().lower()
lst=[]
alp=list(string.ascii_lowercase)
for i in n.split():
    lst.append(i)
s=''
for i in lst:
    sums=0
    for j in range(int(len(i)/2)):
        sums+=alp.index(i[j])-alp.index(i[len(i)-1-j])
    if len(i)%2!=0:
        sums+=alp.index(i[int(len(i)/2)])+1
    s+=str(sums)
print(s)




