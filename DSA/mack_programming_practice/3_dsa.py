#DSA-Assgn-303
#This assignment needs DataStructures.py file in your package, 
#you can get it from resources page
from day2.DataStructures import LinkedList,Queue,Stack
def regenerate_stack(input_stack):
    output_stack = Stack(input_stack.get_max_size())
    #Do Not Change the size of the ouput_stack
    #list1=[]
    new_stack=Stack(input_stack.get_max_size())
    
    while(not input_stack.is_empty()):
        #list1.append(input_stack.pop())
        a=input_stack.pop()
        if(a=="@"):
            new_stack.push(".")
            a=input_stack.pop()
            while(a!="@"):
                new_stack.push(a.upper())
                a=input_stack.pop()
            new_stack.push(".")
        else:
            new_stack.push(a)
    #print(new_stack.__dict__)
    while(not new_stack.is_empty()):
        output_stack.push(new_stack.pop())
        
    '''
    i=list1.index("@")
    j=list1[::-1].index("@")
    j=len(list1)-j
    for m in range(i,j):
        if(list1[m]=="@"):
            list1[m]="."
        else:
            list1[m]=list1[m].upper()
        
    for n in list1[::-1]:
        output_stack.push(n)
    '''
    return output_stack
#You can modify the input to test your code
input_stack = Stack(10)
input_stack.push('stay')
input_stack.push('Happy')
input_stack.push('@')
input_stack.push('infosys')
input_stack.push('in')
input_stack.push('are')
input_stack.push('you')
input_stack.push('@')
input_stack.push('WelCome')
input_stack.push('hi')
output_stack = regenerate_stack(input_stack)
output_stack.display()