#PF-Assgn-30

def encode(message):
    m=""
    count=1
    if(len(message)>1):
        for i in range(0,len(message)-1):
            if(message[i]==message[i+1]):
                count+=1  
            else:
                m+=str(count)+message[i]
                count=1
        m+=str(count)+message[i+1]
        return m
    elif(len(message)==1):
        return "1"+message
    else:
        return -1
    #freq=message.count('A')
    '''
    dict1={}
    for i in message:
        dict1[i]=0
    
    for ch in message:
        dict1[ch]+=1
        
    for k,v in dict1.__iter__():
        m+=str(v)+k
        
    '''
#Provide different values for message and test your program
encoded_message=encode("Affzgggg")
print(encoded_message)