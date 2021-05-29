#Identify palindrome


def reverse(n):
    return int(n[::-1])
n=int(input())
while True:
    if n==reverse(str(n)):
        print(n)
        break
    else:
        n+=reverse(str(n))
    
    
    
