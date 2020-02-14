#PF-Assgn-29
from test.test_xmlrpc import BaseKeepaliveServerTestCase
def calculate(distance,no_of_passengers):
    price_per_litre_of_fuel = 70
    mileage = 10
    price_per_ticket = 80
    invested= (price_per_litre_of_fuel/mileage)*distance
    got= no_of_passengers*price_per_ticket
    
    value = got-invested
    if(value>0):
        return value
    else:
        return -1


#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
