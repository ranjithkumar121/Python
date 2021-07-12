'''Implement the following Function
def ProductSmallestPair(sum, arr)
The function accepts an integers sum and an integer array arr of size n.
Implement the function to find the pair, (arr[j], arr[k]) where j!=k, Such that arr[j] and arr[k] are
the least two elements of array (arr[j] + arr[k] <= sum) and return the product of element of this pair

NOTE

Return -1 if array is empty or if n<2
Return 0, if no such pairs found
All computed values lie within integer range
Example

Input

sum:9

Arr:5 2 4 3 9 7 1

Output

2'''

s=int(input())
arr=list(map(int,input().split()))

arr.sort()
print(arr[0]*arr[1])
