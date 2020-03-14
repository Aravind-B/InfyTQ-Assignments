l1=[1,2,1,4]
# empty list that will store current permutation 
  
def permutation(l1): 
    l = [] 
    for i in range(len(l1)):
        m = l1.pop(0) 
        
        remLst =l1[:i] +l1[i+1:]
      
        if(len(remLst)==3): 
            l.append(remLst)
    return l

print(permutation(l1))