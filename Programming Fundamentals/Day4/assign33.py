#PF-Assgn-33

def find_common_characters(msg1,msg2):
    s=""
    msg=""
    for i in msg1:
        if i in msg2 and i not in s:
            s+=i
    if(s):
        return s
    else:
        return -1
    '''
    abc=set(msg1)&set(msg2)
    a=""
    for i in abc:
        a+=str(i)
    a.replace(" ", "")
    if(a):
        return a
    else:
        return -1
        
        or
        
        ms=list(set(s))
    for i in ms:
        msg+=i
    
    for i in s:
        if j in s:
            if(i==j):
                s=s.replace(i, "")
    '''
#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)