#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data=""
    j=len(list2)-1
    for i in range(len(list1)):
        if((list1[i] is None) or (list2[j] is None)):
            if(list1[i] is None):
                merged_data+=list2[j]+" "
            else:
                merged_data+=list1[i]+" "
        else:
            merged_data+=list1[i]+list2[j]+" "
        j-=1
    return merged_data.strip()

#Provide different values for the variables
# and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)
