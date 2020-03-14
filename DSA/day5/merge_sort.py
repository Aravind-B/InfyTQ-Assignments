list1 = [32, 15, 24, 79, 11, 29, 45]


def merge(left,right):
    k=0
    result=[None]*(len(left)+len(right))
    i=0
    j=0
    while(i<len(left) and j<len(right)):
        for j in range(right):
            if(left[i]<=right[j]):
                result[k]=left[i]
                i+=1
            elif(left[i]>right[j]):
                result[k]=right[j]
                j+=1
            k+=1
    while(i<len(left)):
        result[k]=left[i]
        i+=1
        k+=1
    while(j<len(right)):
        result[k]=right[j]
        j+=1        
        k+=1
                
def merge_sort(input_list):
    if(len(input_list)==1):
        return input_list
    
    else:
        mid=len(input_list)//2
        left_list=merge_sort(input_list[:mid])
        right_list=merge_sort(input_list[mid:])
        return merge(left_list, right_list)
        

    
    
merge_sort(list1)
print(list1)