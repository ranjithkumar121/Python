'''You are required to implement the following Function

def LargeSmallSum(arr)

The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second largest largest element from the even positions and second smallest from the odd position of given ‘arr’

Assumption:

All array elements are unique
Treat the 0th position a seven
NOTE

Return 0 if array is empty
Return 0, if array length is 3 or less than 3
Example

Input

arr:3 2 1 7 5 4

Output

7'''

lenght=int(input())
arr=list(map(int,input().split()))
odd=[]
even=[]
if len(arr)!=0 and len(arr)>3:
    for i in range(lenght):
        if i%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    odd.sort()
    even.sort()

    print(odd[-2]+even[-2])
else:
    print(0)