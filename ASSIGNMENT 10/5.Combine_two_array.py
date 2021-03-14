arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr3=arr1+arr2
for i in arr3:
    if i==arr3[-1]:
        print(i)
    else:

        print(i,end=',')