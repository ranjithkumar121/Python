'''s=input()
word=input()
lst=[]
s1=word.split(":")
for i in s1:
    s2=""
    for j in range(len(i)):
        if s[j]!=s[-1] or s[j]!="_":
            if s[j]!="_":
                if s[j]==i[j]:
                    s2+=i[j]
                else:
                    break
            else:
                if s[j+1]==i[j+1]:
                    s2+=i[j]
        else:
            if s[j-1]==i[j-1]:
                s2+=i[j]
    if len(s2)==len(s):
        lst.append(s2)
for i in lst:
    print(i,end=" ")'''
import string
alp=list(string.ascii_lowercase)
s="_ove"
word="live:love:kove:long".split(":")
lst=[]
ind=s.index("_")
if ind==s[-1]:
    for i in alp:
        lst.append(s[:ind] + i)
elif ind==s[0]:
    for i in alp:
        lst.append(i+s[ind+1:])
else:
    for i in alp:
        lst.append(s[:ind]+i+s[ind+1:])
for i in word:
    if i in lst:
        print(i,end=" ")


