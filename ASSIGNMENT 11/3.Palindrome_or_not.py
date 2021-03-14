def find_palindrome(s1):
    s2 = s1[::-1]
    if s1 == s2:
        print("Palindrome")
    else:
        print("Not a palindrome")
s1=input()
find_palindrome(s1)