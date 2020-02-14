#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    #account_balance=account_balance
    #account_number=["{:1>4}".format(i) for i in range(1000)]
    #acc=for a in xrange(int(0),int(1000))
    #account_number=account_number
    #salary=salary
    #loan_type=loan_type
    #loan_amount_expected=loan_amount_expected
    #customer_emi_expected=customer_emi_expected

    if(account_balance>=100000 and (account_number>999 and account_number<2000)):

        if(salary>25000 and loan_type == "Car"):
            eligible_loan_amount=500000 
            bank_emi_expected=36
        elif(salary>50000 and loan_type == "House"):
            eligible_loan_amount=6000000
            bank_emi_expected=60
        elif(salary>75000 and loan_type == "Business"):
            eligible_loan_amount=7500000
            bank_emi_expected=84
        else:
            print("Invalid loan type or salary")

        if(loan_amount_expected<=eligible_loan_amount and customer_emi_expected<=bank_emi_expected):
            print("Account number:", account_number)
            print("The customer can avail the amount of Rs.", eligible_loan_amount)
            print("Eligible EMIs :", bank_emi_expected)
            print("Requested loan amount:", loan_amount_expected)
            print("Requested EMI's:",customer_emi_expected)
        #else:
        #    print("The customer is not eligible for the loan")
    elif(account_balance<100000 and (account_number>999 and account_number<2000)):
        print("Insufficient account balance")
    elif(account_balance>=100000 and (account_number<1000 or account_number>=2000)):
        print("Invalid account number")
    elif(account_balance<100000 and (account_number<1000 or account_number>=2000)):
        print("Insufficient account balance")
        print("Invalid account number")
    else:
        print("The customer is not eligible for the loan")
#Test your code for different values and observe the results
calculate_loan(1005,20000,255000,"Car",300000,30)