def find(input1):
    b=input1.lower().split()
    alp=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    rr=""
    for i in b:
        lens=len(i)
        r=""
        for j in i:
            r+=alp[(alp.index(j)+lens)%26]
        r=r.capitalize()
        r+=" "
        rr+=r
    return rr


input1=input()
print(find(input1))
