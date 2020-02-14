#PF-Assgn-26
from builtins import int

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    if(legs%2==0 or heads<legs):
        rabbit_count=((legs//2)-heads)
        chicken_count=(heads-rabbit_count)
        print(chicken_count,rabbit_count)
    else:
        print(error_msg)
    #Populate the variables: chicken_count and rabbit_count

#Provide different values for heads and legs and test your program
solve(3,12)