def find_pairs_of_numbers(num_list,n):
    c=0
    for i in range(0,len(num_list)):
        for j in range(i+1,len(num_list)):
            if(num_list[i]+num_list[j]==n):
                c=c+1 
    return(c)
num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))
