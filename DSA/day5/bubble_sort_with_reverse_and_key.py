from day5.init import unit_digit

list1 = [32, 15, 24, 79, 11, 29, 45]


def bubble_sort(input_list,reverse=False,key=None):
    p=0
    for i in range(len(input_list)-1):
        p+=1
        print("Pass",p)
        swapped=False
        for j in range(len(input_list)-i-1):
            if(key==None):
                val1=input_list[j]
                val2=input_list[j+1]
            else:
                val1=key(input_list[j])
                val2=key(input_list[j+1])
            if((not reverse and val1>val2) or (reverse and val1<val2)):
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                swapped=True
        if(not swapped):
            break
 
      
bubble_sort(list1,True)
print(list1)

bubble_sort(list1)
print(list1)


bubble_sort(list1, key=unit_digit, reverse=True)
print(list1)