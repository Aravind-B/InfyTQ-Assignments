#PF-Exer-28
from statistics import mode                                             
#This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    team1=match_tuple.count("Team1")
    team2=match_tuple.count("Team2")
    
    if(team1>team2):
        return "Team1"
    elif(team2>team1):
        return "Team2"
    else:
        return "Tie"
#Invoke the function with each of the print statements given below
print(find_winner_of_the_day("Team1","Team2","Team1"))
#print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))