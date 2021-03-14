def isBalanced(s):
    c1=s.count("{")
    c2=s.count("}")
    if c1==c2:
        return True
    else:
        return False
s=input()
print(isBalanced(s))