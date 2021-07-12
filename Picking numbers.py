#Given an array of integers, find the longest subarray where the absolute difference between any
# two elements is less than or equal to 1.

def pickingNumbers(a):
    m = 0
    for i in range(len(a)):
        g = 1
        l = 1
        for j in range(len(a)):
            if i != j:
                if a[i] == a[j] or a[i] + 1 == a[j]:
                    g += 1
                if a[i] == a[j] or a[i] - 1 == a[j]:
                    l += 1
        if g > l:
            if g > m:
                m = g
        else:
            if l > m:
                m = l
    return m




n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = pickingNumbers(a)
print(result)

