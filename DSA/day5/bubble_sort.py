list1 = [32, 15, 24, 79, 11, 29, 45]


def bubble_sort(input_list):
    p=0
    for i in range(len(input_list)-1):
        p+=1
        print("Pass",p)
        swapped=False
        for j in range(len(input_list)-i-1):
            if(input_list[j]>input_list[j+1]):
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                swapped=True
        if(not swapped):
            break
     
bubble_sort(list1)
print(list1)
