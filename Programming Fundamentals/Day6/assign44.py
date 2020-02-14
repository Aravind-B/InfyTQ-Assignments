#PF-Assgn-44

def find_duplicates(list_of_numbers):
    list1=[]
    for i in set(list_of_numbers):
        if(list_of_numbers.count(i)>1):
            list1.append(i)
    return list1

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)