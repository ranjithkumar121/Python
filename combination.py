s=input()
def combination(s):
    if len(s)==0:
        return []
    if len(s)==1:
        return [s]
    l=[]
    for i in range(len(s)):
        m=s[i]
        S=s[:i]+s[i+1:]
        for c in combination(S):
            l.append(m+c)
    return l

lst=combination(s)
for i in lst:
    print(i,end=" ")