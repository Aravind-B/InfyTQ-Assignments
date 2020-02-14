#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    count=0
    avg=sum(list_of_marks)/len(list_of_marks)
    for i in list_of_marks:
        if(i>avg):
            count+=1
    return ((count/len(list_of_marks))*100)

def sort_marks():
    list1=list(list_of_marks)
    return sorted(list1)

def generate_frequency():
    list2=[]
    for i in range(26):
        if(i in list_of_marks):
            list2.append(list_of_marks.count(i))
        else:
            list2.append(0)
    return list2
    
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())