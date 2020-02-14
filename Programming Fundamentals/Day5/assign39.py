#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,3,0]

'''This method accepts the item followed by the quantity required by a customer in the format item1, quantity_required, item2, quantity_required etc.'''
def place_order(*item_tuple):
    a=item_tuple
    list1=[]
    list2=[]
    for j in a:
        if(isinstance(j, str)):
            list1.append(j)
    for j in a:
        if(isinstance(j, int)):
            list2.append(j)
    #print(type(a[3]))
    #quantity_requested=[]
    for i in range(len(list1)):
        if(list1[i] in menu):
            quantity_requested=list2[i]
            index1=menu.index(list1[i])
            b=check_quantity_available(index1, quantity_requested)
            if(not b):
                print ("%s stock is over" %(list1[i]))
            else:
                print ("%s is available" % (list1[i]))
        else:
            print("%s is not available" %(list1[i]))
    #Populate the item name in the below given print statements
    #Use it to display the output wherever applicable
    #Also, do not modify the text in it for verification to work
    
    #print("<item name>is not available")
    #print("<item name>stock is over")
    #print ("<item name>is available")


'''This method accepts the index position of the item requested by the customer in the quantity_available list, and the requested quantity of the item.'''
def check_quantity_available(index,quantity_requested):
    if(quantity_available[index]>=quantity_requested):
        quantity_available[index]-=quantity_requested
        #print(quantity_available)
        return True
    else:
        return False

#Provide different values for items ordered and test your program
place_order("Fried Rice",2,"Soup",1)
#place_order()
#place_order("Soup",1,"Veg Roll", 2, "Fried Rice1",1)