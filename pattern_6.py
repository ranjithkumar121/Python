#Display reverse number pattern
'''
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
'''

row=5
for i in range(row+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
