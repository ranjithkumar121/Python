def find_count(word):
    count=0
    num="1234567890"
    for letter in word:
        if letter not in num and letter!=' ':
            count+=1
        else:
            pass
    return count
word=input()
print(find_count(word))