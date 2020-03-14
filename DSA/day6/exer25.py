#DSA-Exer-25

def find_maximum_activities(activity_list,start_time_list, finish_time_list):
    for i in range(len(activity_list)-1):
        swapped=False
        for j in range(len(activity_list)-i-1):
            if(finish_time_list[j]>finish_time_list[j+1]):
                finish_time_list[j],finish_time_list[j+1] = \
                finish_time_list[j+1],finish_time_list[j]
                
                activity_list[j], activity_list[j+1] = \
                activity_list[j+1], activity_list[j]
                
                start_time_list[j], start_time_list[j+1] = \
                start_time_list[j+1], start_time_list[j]
                
                swapped= True
                
        if(not swapped):
            break
    
    #GREEDY
    
    events=[]
    pointer=0
    events.append(activity_list[pointer])
    attended=pointer
    pointer+=1
    while(pointer<len(activity_list)):
        if(finish_time_list[attended]+1 <= start_time_list[pointer]):
            events.append(activity_list[pointer])
            attended=pointer
            pointer+=1
        else:
            pointer+=1
            
    return events
    
    
#Pass different values to the function and test your program
activity_list=[1,2,3,4,5,6,7]
start_time_list=[1,4,2,3,6,8,6]
finish_time_list=[2,6,4,5,7,10,9]

print("Activities:",activity_list)
print("Start time of the activities:",start_time_list)
print("Finishing time of the activities:", finish_time_list)

result=find_maximum_activities(activity_list,start_time_list, finish_time_list)
print("The maximum set of activities that can be completed:",result)