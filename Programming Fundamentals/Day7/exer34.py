#PF-Exer-34
import math
def combi(num1,num2):
    return (math.factorial(num1))/((math.factorial(num1-num2))*(math.factorial(num2)))
            
def find_number_of_combination(number_of_flavours):
    total_combination=0
    
    for i in range(number_of_flavours+1):
        total_combination+=combi(number_of_flavours,i)

    return total_combination


#Provide different values for number_of_flavours and test your program
number_of_combination=find_number_of_combination(4)
print(number_of_combination)