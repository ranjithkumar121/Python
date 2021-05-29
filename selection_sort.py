def selection_sort(lst):
    for i in range(len(lst)):
        min_value=i
        for j in range(i+1,len(lst)):
            if lst[min_value]>lst[j]:
                min_value=j
        lst[i],lst[min_value]=lst[min_value],lst[i]
    return lst
lst=[4,8,1,8,10,2,5]
print(selection_sort(lst))