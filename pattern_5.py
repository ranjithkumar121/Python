#Display descending order of number
'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
'''
row=5
for i in range(row,0,-1):
    num=i
    for j in range(1,i+1):
        print(num,end=" ")
    print()
