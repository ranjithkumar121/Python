def insertion_sort(lst):
    for i in range(1,len(lst)):
        j=i
        while lst[j-1] > lst[j] and j>0:
            lst[j],lst[j-1]=lst[j-1],lst[j]
            j-=1
    return lst
lst=[4,8,1,8,10,2,5]
print(insertion_sort(lst))