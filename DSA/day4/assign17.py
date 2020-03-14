#DSA-Assgn-17

def find_matches(country_name):
    list1=[]
    for i in match_list:
        if(i.startswith(country_name)):
            list1.append(i)
    return list1

def max_wins():
    dict1={}
    for match in match_list:
        k1=match.split(":")
        k=k1[1]
        win=int(k1[3])
        
        if k not in dict1.keys():
            dict1[k]=win
        '''
        if dict1[k] is None:
            dict1[k]=win
        '''
        if dict1[k]>=0:
            if dict1[k]<win:
                dict1[k]=win
    temp=dict1.copy()
    
    for key in dict1:
        dict1[key]=[]
    for match in match_list:
        k1 = match.split(":")
        k=k1[1]
        win=int(k1[3])
        if win==temp[k]:
            dict1[k].append(k1[0])
    return dict1

def find_winner(country1,country2):
    total1=0
    total2=0
    for match in match_list:
        k1=match.split(":")
        if(k1[0].startswith(country1)):
            total1+=int(k1[3])
        
        if(k1[0].startswith(country2)):
            total2+=int(k1[3])
    
    if(total1>total2):
        return country1
    elif(total1<total2):
        return country2
    else:
        return "Tie"
        

#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3",
            "IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0",
            "SA:CHAM:5:1","SA:T20:5:0"]

#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print()
max_wins()