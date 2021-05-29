#Inverted pyramid pattern with same number
'''
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
'''
a=int(input("Enter the number:"))
row=5
for i in range(row,0,-1):
    for j in range(1,i+1):
        print(a,end=" ")
    print()
