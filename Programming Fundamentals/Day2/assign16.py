#PF-Assgn-16

def make_amount(rupees_to_make,no_of_five,no_of_one):
    remain_five=no_of_five
    remain_one=no_of_one
    
    five_needed=rupees_to_make//5
    one_needed=rupees_to_make%5
    
    if(five_needed>remain_five):
        one_needed=one_needed+5*(five_needed-remain_five)
        remain_five=0
    else:
        remain_five=remain_five-five_needed
    #one_needed=5*five_needed+no_of_one-rupees_to_make+1
    
    '''
    if(one_needed>remain_one):
        one_needed=remain_one
    else:
        remain_one=remain_one-one_needed
    '''
    remain_one=remain_one-one_needed
    five_needed=no_of_five-remain_five
    one_needed=no_of_one-remain_one
    #Populate the variables: five_needed and one_needed


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    

    if(rupees_to_make>5*no_of_five+no_of_one):
        print(-1)
    else:
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
#Provide different values for rupees_to_make,
#no_of_five,no_of_one and test your program
make_amount(105,19,3)
