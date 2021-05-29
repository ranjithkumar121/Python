def find_pairs_of_numbers(num_list,n):
    count = 0
    for i in range(0,len(num_list)-1):
        for j in range(i+1,len(num_list)):
            current_value=num_list[i]
            next_value=num_list[j]
            if current_value>n:
                break
            elif current_value+next_value==n:
                count+=1
                break
    if count!=0:
        return count
    else:
        return 0

num_list=[1, 2, 7, 4, 5, 6, 0, 3]
n=6
print(find_pairs_of_numbers(num_list,n))