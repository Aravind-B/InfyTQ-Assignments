#PF-Exer-35

def count_names(name_list):
    count1=0
    count2=0
    
    for i in name_list:
        if(i.endswith("at") and len(i)==3):
            count1+=1
        
        try:
            if(i.index("at") or i.endswith("at") or i.startswith("at")):
                count2+=1
        except:
            pass
            
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print("_at -> ",count1)
    print("%at% -> ",count2)

#Provide different names in the list and test your program
name_list=['GOAT', 'atter', 'at']
count_names(name_list)