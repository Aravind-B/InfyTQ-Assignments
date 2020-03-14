list1 = [32, 15, 24, 79, 11, 29, 45]

def our_min(input_list, start_index):
    min_ind = start_index
    for i in range(start_index + 1, len(input_list)):
        if(input_list[i] < input_list[min_ind]):
            min_ind = i
    return min_ind

def selection_sort(input_list):
    for i in range(len(input_list)-1):
        m = our_min(input_list,i)
        input_list[i], input_list[m] = input_list[m], input_list[i]
     
selection_sort(list1)
print(list1)
