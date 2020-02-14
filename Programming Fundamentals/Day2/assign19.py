#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    price1=0
    price2=0
    if(food_type=="N" and distance_in_kms>0 and quantity_ordered>0):
        price1=quantity_ordered*150
        if(distance_in_kms<=3):
            bill_amount=price1
        elif(distance_in_kms>3 and distance_in_kms<=6):
            bill_amount=price1+3*(distance_in_kms)
        else:
            bill_amount=price1+9+6*(distance_in_kms-6)
            
    elif(food_type=="V" and distance_in_kms>0 and quantity_ordered>0):
        price2=quantity_ordered*120
        if(distance_in_kms<=3):
            bill_amount=price2
        elif(distance_in_kms>3 and distance_in_kms<=6):
            bill_amount=price2+3*(distance_in_kms)
        else:
            bill_amount=price2+9+6*(distance_in_kms-6)
    else:
        bill_amount=-1
    return bill_amount
    #Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("V",1,7)
print(bill_amount)