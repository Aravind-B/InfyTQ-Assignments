#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    flag=0
    for i in reqd_gems:
        #temp=i
        index1=reqd_gems.index(i)
        quant1=reqd_quantity[index1]
        if i in gems_list:
            index2=gems_list.index(i)
            price=price_list[index2]
            bill_amount+=(price*quant1)
            #bill_amount=-1
    if(flag!=1):
        if(bill_amount>30000):
            bill_amount-=0.05*bill_amount
        return bill_amount
    else:
        return -1

#List of gems available in the store
#gems_list=['Moonstone', 'Sapphire', 'Quartz']
gems_list=['Amber', 'Aquamarine', 'Opal', 'Topaz']
#Price of gems available in the store. 
#gems_list and price_list have one-to-one correspondence
#price_list=[3498, 1257, 5467]
price_list=[4392, 1342, 8734, 6421]
#List of gems required by the customer
#reqd_gems=['Ivory', 'Quartz']
reqd_gems=['Amber', 'Opal', 'Topaz']
#Quantity of gems required by the customer. reqd_gems 
#and reqd_quantity have one-to-one correspondence
#reqd_quantity=[5,8]
reqd_quantity=[2, 1, 3]
bill_amount=calculate_bill_amount(gems_list, 
price_list, reqd_gems, reqd_quantity)
print(bill_amount)